import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASEDIR,'log/system.log')
REPORT_DIR = os.path.join(BASEDIR,'report/')
#DATABASE = 'D:\yangjian\project\web_demo\django_web\db.sqlite3'
DATABASE = 'F:\work\project\django_web\db.sqlite3'
master_url = "http://127.0.0.1:8090/slave_heartbeat"
masterip = '127.0.0.1'
slaveip = '1.1.1.1'
heartbeat = 10
slave_label = 'test1'  #
taskqueue = 'test1'

#ui
UICASE_DIR = os.path.join(BASEDIR,'cases/ui/')
UI_RESULT_TABLE = 'ui_result_table'

#api
APICASE_DIR = os.path.join(BASEDIR,'cases/api/')
Interface_Time_Out = 10
API_RESULT_TABLE = 'api_result_table'

