from pymongo import MongoClient
import config as CONFIG
host = '127.0.0.1'
client = MongoClient(CONFIG.MONGO_IP,CONFIG.MONGO_PORT)
# db = client.test1
# client.admin.authenticate('root','123456',mechanism='SCRAM-SHA-1')
my_db = client['test1']
collection = my_db.coll
collection.insert({"name":'na2','id':2})