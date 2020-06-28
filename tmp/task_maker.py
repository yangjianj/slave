from lib.redisConnector import Connector
import config as CONFIG

if __name__ == '__main__':
    task = {
        "id": "taskid123456",
        "name": "name123",
        "slave": "slave1",
        "version": "version001",
        "project": "pro1",
        "cases": ["suite1", "suite111", "suite2", "suite211", "suite3", "suite311", "suite411", "suite4"]
    }
    redis = Connector()
    redis.publish(CONFIG.TASK_TOPIC,task)