# -*- coding: utf-8 -*-
import os,sys
import config
from lib.runner import UiRunner, ApiRunner

sys.path.append(config.ROBOT_PATH)
from robotRunner.run import Runner

class Exector():
    def __init__(self):
        pass

    def task_handler(self, task):
        re = self.run(task)
        self.finish_task(task)
        self.upload_report(task)

    def run(self, task):
        
        robotrunner = Runner()
        robotrunner.run_task(taskparam)
        
        # if task["type"] == "ui":
        #     uiTaskManager(task).run()
        # elif task["type"] == "api":
        #     runner = ApiRunner(task)
        #     return runner.run()

    def finish_task(self, task):
        #执行完task后更新task状态到master
        pass

    def upload_report(self, report):
        #上传ui test report到ftp server
        pass


if __name__ == "__main__":
    '''
    task = {"id": 5662356461,
            "type": "api",
            "slave": "1.1.1.1",
            "version": "0.0.1",
             "cases": [
                     {"caseid": "api_00002",  "project": "wuliu", "api_name": "login",
                      "url": "http://www.kuaidi100.com/query",
                      "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                      "params":{"type":"yunda","postid":"3835494398576"},
                      "data": '{"q":"w"}',
                      "status":"unfinished",
                      "expected": {"type": "object",
                                   "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                  "data": {"type": "array"}}}},
                     {"caseid": "api_00001", "project": "wuliu", "api_name": "login",
                      "url": "http://www.kuaidi100.com/query",
                      "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                      "params":{"type":"yuantong","postid":"823753023765"},
                      "data": '{"q":"w"}',
                      "status":"unfinished",
                      "expected": {"type": "object",
                                   "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                  "data": {"type": "array"}}}}
                 ]
                     }
    '''
    task = {"id": 5662356461,
            "type": "ui",
            "slave":"1.1.1.1",
            "version": "0.0.1",
            "project": "lianjia",
             "cases": [
                    {"caseid": "test1", "function": "login","status":"unfinished"},
                    {"caseid": "test2", "function": "login","status":"unfinished"},
                     ]
                     }
    robottask = {
    "outputdir":outputdir,
    "taskname":"taskname",
    "include":"para-test",
    "suite":"",
    "suitedir":"uitest_base",
    "variable":{"taskid":"taskid12345"}
    }
    
    Exector().task_handler(task)
