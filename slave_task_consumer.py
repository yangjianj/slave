# -*- coding: utf-8 -*-
import pika,threading
import requests,time,datetime,json
from lib.taskManager import TaskManager
from lib.redisConnector import Connector
import config

#rabbitmq消费消息回调函数
def callback(ch, method, properties, body):
    print("-->ch", ch)
    print("-->method", method)
    print("-->properties", properties)
    print("[x] Received %r" % body)  # 一条消息被一个消费者接收后，该消息就从队列删除

    Exector().task_handler(body)  #处理任务
    ch.basic_ack(delivery_tag=method.delivery_tag)

#rabbitmq消费端
def run_rabbitmq():
    con = pika.ConnectionParameters(config.masterip)
    connection = pika.BlockingConnection(con)
    channel = connection.channel()
    channel.queue_declare(queue=config.taskqueue)  # 声明队列，保证程序不出错
    channel.basic_consume(config.taskqueue,callback)

    print('[*] Waiting for messages.To exit press CTRL+C')
    channel.start_consuming()

#redis作为消息队列消费消息
def run_redis():
    redis_cli = Connector()
    for item in redis_cli.subscribe(config.TASK_TOPIC):
        print(item)
        try:
            task = json.loads(item["data"])
            print(task)
            # Exector().task_handler(task)
        except Exception as e:
            print(e)
#slave心跳
def heartbeat():
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

if __name__ == '__main__':
    # threading.Thread(target = heartbeat,args = ()).start()
    # run_redis()
    task = {
        "id": "taskid123456",
        "name": "name123",
        "slave": "slave1",
        "version": "version001",
        "project": "pro1",
        "cases": ["suite1", "suite111", "suite2", "suite211", "suite3"]
    }
    tm = TaskManager(task)
    tm.run()