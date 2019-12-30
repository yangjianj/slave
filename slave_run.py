# -*- coding: utf-8 -*-
from flask import Flask
import requests,time,datetime,json
import threading
import config
from lib.log_manager import LogManager
import lib.sys_param as sysparam

app= Flask(__name__)

@app.route("/")
def index():
    return '<h1> hello flask !</h1>'

@app.route("/get_json")
def get_json():
    return '{"code": 0,"payload": [{"省份": "湖南省","时间": "2019-07-10",}, {"省份": "湖北省","时间": "2019-07-15", },' \
           '{"省份": "深圳市","时间": "2019-08-02", }, {  "省份": "广东省", "时间": "2019-08-15", }],"errmsg": ""}'

def heartbeat():  #slave心跳
    while(1):
        try:
            url = config.master_url
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = {"ip":config.slaveip,"timestamp":timestamp}
            data = json.dumps(data)
            headers = {
                'content-type': "application/json",
            }
            response = requests.request("POST",url,data=data,headers=headers).text
            response = json.loads(response)
            if  response["status"] == "true":
                print("connect master succeed")
            else:
                print(response["message"])
        except Exception as error:
            print("connect master failed:"+str(error))
        finally:
            time.sleep(config.heartbeat)

@app.route("/get_sys_params")
def system_param():
    result = {}
    result['net_if'] = sysparam.collect_net_if_addrs()
    result['net_io'] = sysparam.collect_net_io()
    result['cpu'] = sysparam.collect_cpu()
    result['memery'] = sysparam.collect_memery()
    result['disk'] = sysparam.collect_disk()
    return result

@app.route("/run_cmd")
def run_cmd():
    pass

if __name__=="__main__":
    #threading.Thread(target = heartbeat,args = ()).start()  #心跳挪到slave_task_consumer中
    app.run(host='0.0.0.0', port=8080, debug=True)