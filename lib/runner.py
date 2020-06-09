# -*- coding: utf-8 -*-
import unittest
from lib.HtmlTestRunner import HTMLTestRunner
from lib.apiTest import Apiclient
from lib.tool import *
from lib.mysqlConnector import  DataManager
from lib.logManager import LogManager
import config
'''
负责任务执行，生产log文件
'''
class ApiRunner():
    '''
    api执行器类：通过任务初始化对象：
        task = {"id": 5662356461,
            "type": "api",
            "data": {"project": "pro1",
                     "version": "0.0.1",
                     "cases": [
                         {"caseid": "api_001", "version": "0.01", "project": "wuliu", "api_name": "login",
                          "url": "http://www.kuaidi100.com/query",
                          "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                          "params":{"type":"yunda","postid":"3835494398576"},
                          "data": '{"q":"w"}',
                          "expected": {"type": "object",
                                       "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                      "data": {"type": "array"}}}},
                         {"caseid": "api_001", "version": "0.01", "project": "wuliu", "api_name": "login",
                          "url": "http://www.kuaidi100.com/query",
                          "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                          "params":{"type":"yuantong","postid":"823753023765"},
                          "data": '{"q":"w"}',
                          "expected": {"type": "object",
                                       "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                      "data": {"type": "array"}}}}
                     ]
                     }}
    '''
    def __init__(self,task):
        self.all_cases = task["cases"]
        self.version = task["version"]
        self.taskid = task["id"]
        self.table=config.API_RESULT_TABLE
        self.logger=LogManager()

    def run(self):
        #执行任务并返回任务执行状态
        result=[]
        for case in self.all_cases:
            client = Apiclient(case)
            re=client.test()
            re["case"]=case
            self._save_result(re)  #每执行完一条case就存储到数据库
            result.append(re)
        return result

    def _save_result(self,apiresult):
        if ("response" in apiresult["re"]):
            result = apiresult["re"]["test_result"]
            response = apiresult["re"]["response"]
        elif ("error" in apiresult["re"]):
            response = apiresult["re"]["error"]
            result = "error"
        else:
            response = apiresult["error"]
            result = "error"
        caseid = apiresult["case"]['caseid']
        spend = apiresult["spend"]
        starttime = apiresult["start-time"]
        endtime = apiresult["end-time"]
        db=DataManager()
        message =db.save_api_result(self.taskid,caseid,result,response,spend,starttime,endtime)
        if message != True:
            self.logger.error(message)

class UiRunner():
    '''
    初始化信息：执行的case目录，所需执行文件list
    执行内容：执行指定脚本信息，并返回执行结果信息
    '''
    def __init__(self,taskid,workdir,reportdir=None,tasklist=None):
        dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.taskid = taskid
        self.tasklist = tasklist
        self.workdir = workdir
        if reportdir == None:
            self.reportfile = os.path.join(workdir,'report',dt+'htmltestrunner.html')
        else:
            self.reportfile = os.path.join(reportdir, dt + 'htmltestrunner.html')
        self.table = config.UI_RESULT_TABLE
        self.logger = LogManager()

    #根据文件名匹配case 每个ui任务包含十个case
    def run_by_pattern(self,filelist):
        discover = None
        for index,item in enumerate(filelist):
            if index == 0:
                discover = unittest.defaultTestLoader.discover(self.workdir, pattern=item, top_level_dir=None)
            else:
                discover_tmp = unittest.defaultTestLoader.discover(self.workdir, pattern=item, top_level_dir=None)
                discover.addTests(discover_tmp._tests)
        all_result = self._run_generate_log(discover)
        return all_result

    #根据case名匹配case
    def run_by_casename(self,namelist):
        #caselist = ['lianjia.ui_lianjia_test_001.Base_t1.test_run3','lianjia.ui_lianjia_test_001.Base_t1.test_run']
        discover = unittest.TestLoader().loadTestsFromNames(namelist,module=None)
        all_result = self._run_generate_log(discover)
        return all_result
    
    def run_by_dir(self,casedir):
        discover = unittest.defaultTestLoader.discover(casedir,pattern='test*.py',top_level_dir=None)
        all_result= self._run_generate_log(discover)
        return all_result

    def _run_generate_log(self,discovered):
        with open(self.reportfile,'wb') as f:
            runner = HTMLTestRunner(stream=f,
                                    verbosity=2,
                                    title='my report',
                                    description='generated by htmltestrunner')
            all_result = runner.run(discovered)
        return all_result

    def run(self):
        if self.tasklist == None:
            result = self.run_by_dir(self.workdir)
        self._save_result(result)
        return 1

    def _save_result(self,result):
        '''
        #存储测试结果到对应数据库
        print(result.result)
        print(result.success_count)
        print(result.error_count)
        print(result.failure_count)
        print(result.starttime)
        print(result.endtime)
        '''
        result_map = ['pass', 'fail', 'error']
        db = DataManager()

        for item in result.result:
            status = result_map[item[0]]
            caseid = str(item[1])
            print('########################')
            print(caseid)
            message = item[2]
            error = item[3]
            starttime = item[4]
            endtime = item[5]
            re = db.save_ui_result(self.taskid,caseid,status,message,error,starttime,endtime)
            if re != True:
                self.logger.error(re)


if __name__=="__main__":
    cc=UiRunner(1)
    cc.run()