# -*- coding: utf-8 -*-
import config
from lib.runner import UiRunner,ApiRunner

class Exector():
    def __init__(self):
        pass

    def task_handler(self,task):
        #{'id':1256635665,'type':'ui','data':{'version':'0.0.1','function':'login'}}
        #{'id':5662356461,'type':'ui','data':{'version':'0.0.1','cases':[csv-row1,csv-row1,]}}
        if task['type'] == 'ui':
            self.run_ui(task)
        elif task['type'] == 'api':
            self.run_api(task)
        self.finish_task()

    def run_ui(self,task):
        runner = UiRunner(task)
        runner.run()

    def run_api(self,task):
        runner = ApiRunner(task)
        runner.run()

    def finish_task(self,task):
        #推送任务执行报告
        pass

    def upload_report(self,report):
        pass
