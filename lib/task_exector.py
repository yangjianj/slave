# -*- coding: utf-8 -*-
import config
from lib.runner import UiRunner, ApiRunner

class Exector():
    def __init__(self):
        pass

    def task_handler(self, task):
        # {"id":1256635665,"type":"ui","data":{"project":"pro1","version":"0.0.1","function":"login"}}
        # {"id":5662356461,"type":"ui","data":{"project":"pro1","version":"0.0.1","cases":[csv-row1,csv-row1,]}}
        re = self.run(task)
        self.finish_task(task)
        self.upload_report(task)

    def run(self, task):
        if task["type"] == "ui":
            runner = UiRunner(task)
            return runner.run()
        elif task["type"] == "api":
            runner = ApiRunner(task)
            return runner.run()

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
            "data": {"project": "pro1",
                     "version": "0.0.1",
                     "cases": [
                         {"caseid": "api_001", "version": "0.01", "project": "wuliu", "api_name": "login",
                          "url": "http://www.kuaidi100.com/query",
                          "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                          "params":{"type":"yunda","postid":"3835494398576"},
                          "data": '{"q":"w"}',
                          "status":"unfinished",
                          "expected": {"type": "object",
                                       "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                      "data": {"type": "array"}}}},
                         {"caseid": "api_001", "version": "0.01", "project": "wuliu", "api_name": "login",
                          "url": "http://www.kuaidi100.com/query",
                          "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                          "params":{"type":"yuantong","postid":"823753023765"},
                          "data": '{"q":"w"}',
                          "status":"unfinished",
                          "expected": {"type": "object",
                                       "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                      "data": {"type": "array"}}}}
                     ]
                     }}
    '''
    task = {"id": 5662356461,
            "type": "ui",
            "data": {"project": "lianjia",
                     "version": "0.0.1",
                     "cases": [
                         {"suitename": "ui_lianjia_test_001", "version": "0.01", "project": "lianjia", "function": "login","status":"unfinished"},
                         {"suitename": "ui_lianjia_test_001", "version": "0.01", "project": "lianjia", "function": "login","status":"unfinished"},
                     ]
                     }}
    Exector().task_handler(task)
