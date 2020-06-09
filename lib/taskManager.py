# -*-coding:UTF-8 -*-
import os,time
import config as CONFIG
import lib.taskFileHandler as taskFileHandler
from lib.runner import UiRunner, ApiRunner
'''
负责任务管理：创建工作目录，报告目录，下载case，使用runner执行任务，任务结果存储到数据库
'''
class uiTaskManager():
    def __init__(self,task):
        self.id = task['id']
        self.runSlave = task['slave']
        self.version = task['version']
        self.project = task['project']
        self.cases = task['cases']
        self.work_dir = None
        self.report_dir = None
    
    def _create_work_dir(self):
        wt = time.strftime("%Y-%m-%d-%H-%M-%S")
        self.work_dir = os.path.join(CONFIG.LOCAL_CASE_PATH,'version_'+self.version+'_'+wt)
        self.report_dir = os.path.join(CONFIG.LOCAL_REPORT_PATH,'version_'+self.version+'_'+wt)
        os.makedirs(self.work_dir)
        os.makedirs(self.report_dir)
        
    def download_case(self):
        self._create_work_dir()
        caseidlist = []
        for item in self.cases:
            caseidlist.append(item['caseid'])
        taskFileHandler.download_tasklist(caseidlist,self.work_dir)
    
    def serach_case_ftppath(self,caselist):
        #寻找uicase路径并返回
        for i in caselist:
            pass
    
    def run(self):
        self.download_case()
        runner = UiRunner(self.id,self.work_dir,self.report_dir)
        #runner = UiRunner("E:\\localcase\\version_0.0.1_2020-06-08-23-05-22", self.report_dir)
        return runner.run()
