# -*-coding:UTF-8 -*-
import sys,os,time
import config as CONFIG
from lib.taskFileHandler import TaskFileHandler
from lib.runner import UiRunner, ApiRunner
sys.path.append(CONFIG.ROBOT_PATH)
print(sys.path)
from robotRunner.run import Runner
'''
负责任务管理：创建工作目录，报告目录，下载case，使用runner执行任务，任务结果存储到数据库
'''
class TaskManager():
    def __init__(self,task):
        self.id = task['id']
        self.name = task["name"]
        self.runSlave = task['slave']
        self.version = task['version']
        self.project = task['project']
        self.cases = task['cases']
        self.work_dir = None
        self.report_dir = None
        self.TaskFileHandler = TaskFileHandler()
    
    def _create_work_dir(self):
        wt = time.strftime("%Y-%m-%d-%H-%M-%S")
        self.work_dir = os.path.join(CONFIG.LOCAL_CASE_PATH,'version_'+self.version+'_'+wt)
        self.report_dir = os.path.join(CONFIG.LOCAL_REPORT_PATH,'version_'+self.version+'_'+wt)
        os.makedirs(self.work_dir)
        os.makedirs(self.report_dir)
        
    def download_case(self):
        print("start download cases")
        self._create_work_dir()
        self.TaskFileHandler.download_tasklist(self.cases,self.work_dir)
        print("finished download cases")
    
    def serach_case_ftppath(self,caselist):
        #寻找uicase路径并返回
        for i in caselist:
            pass
    
    def run(self):
        self.download_case()
        taskparam= {
            "outputdir": self.report_dir,
            "taskname": self.name,
            "include": '',
            "suite": '',
            "suitedir": self.work_dir,
            "variable": {"taskid":self.id,"name":"myname"}
        }
        runner = Runner()
        runner.run_task(taskparam)
        # runner = UiRunner(self.id,self.work_dir,self.report_dir)
        # runner = UiRunner("E:\\localcase\\version_0.0.1_2020-06-08-23-05-22", self.report_dir)
        return True

if __name__ == '__main__':
    task = {
        "id":"taskid123456",
        "name":"name123",
        "slave":"slave1",
        "version":"version001",
        "project":"pro1",
        "cases":["suite1","suite111","suite2","suite211","suite3"]
    }
    tm= TaskManager(task)