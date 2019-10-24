# -*- coding: utf-8 -*-
import config
from lib.runner import UiRunner, ApiRunner

class Exector():
    def __init__(self):
        pass

    def task_handler(self, task):
        # {'id':1256635665,'type':'ui','data':{'project':'pro1','version':'0.0.1','function':'login'}}
        # {'id':5662356461,'type':'ui','data':{'project':'pro1','version':'0.0.1','cases':[csv-row1,csv-row1,]}}
        self.run(task)
        self.finish_task(task)
        self.upload_report(task)

    def run(self, task):
        if task['type'] == 'ui':
            runner = UiRunner(task)
            runner.run()
        elif task['type'] == 'api':
            runner = ApiRunner(task)
            runner.run()

    def finish_task(self, task):
        pass

    def upload_report(self, report):
        pass


if __name__ == '__main__':
    task = {'id': 5662356461,
            'type': 'api',
            'data': {'project': 'pro1',
                     'version': '0.0.1',
                     'cases': [
                         {'caseid': 'api_001', 'version': '0.01', 'project': 'wuliu', 'api_name': 'login',
                          'url': 'http://www.kuaidi100.com/query',
                          'protocol': 'http', 'headers': 'ss', 'method': 'post',
                          'data': {"type": "yunda", "postid": "3835494398576"},
                          'expected': {"type": "object",
                                       "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                      "data": {"type": "array"}}}},
                         {'caseid': 'api_001', 'version': '0.01', 'project': 'wuliu', 'api_name': 'login',
                          'url': 'http://www.kuaidi100.com/query',
                          'protocol': 'http', 'headers': 'ss', 'method': 'post',
                          'data': {"type": "yunda", "postid": "3835494398576"},
                          'expected': {"type": "object",
                                       "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                      "data": {"type": "array"}}}}
                     ]
                     }}

    Exector().task_handler(task)
