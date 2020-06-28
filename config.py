import os

master_url = "http://127.0.0.1:8090/slave_heartbeat"
masterip = '127.0.0.1'
slaveip = '1.1.1.1'
heartbeat = 10
slave_label = 'test1'  #
taskqueue = 'test1'

BASEDIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASEDIR,'output/log/system.log')
OUTPUT = os.path.join(BASEDIR,'output/')
#DATABASE = 'E:\yangjian\project\web_demo\django_web\db.sqlite3'
DATABASE = 'F:\work\project\django_web\db.sqlite3'
TASK_TABLE = 'task_table'  # ui and api task
UI_TASK_CASE_TABLE = 'ui_task_case_table'
API_TASK_CASE_TABLE = 'ui_task_case_table'

#ui
UICASE_DIR = os.path.join(BASEDIR,'cases/ui/')
UI_REPORT_DIR = os.path.join(BASEDIR,'output/report/')

FTPSERVER = '127.0.0.1'
FTP_USERNAME = 'uitest'
FTP_PASSWORD = 'uitest'
UI_CASE_DIR = 'UICASE/'
MONITOR_BASEDIR = 'E:/tmp'

#api
APICASE_DIR = os.path.join(BASEDIR,'cases/api/')
Interface_Time_Out = 10
API_RESULT_TABLE = 'api_result_table'

#redis配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
TASK_TOPIC = 'task'

#mongo配置
MONGO_IP = '127.0.0.1'
MONGO_PORT = 27017
MONGO_USER = ''
MONGO_PWD = ''
AUTO_DB = 'autotest'


LOCAL_CASE_PATH = 'E:\\localcase'
LOCAL_REPORT_PATH = 'E:\\report'

ROBOT_PATH = "F:\\work\project\\"