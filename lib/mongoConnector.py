# -*- coding: utf-8 -*-
from pymongo import MongoClient
import config as CONFIG

class MongoConnector():
    def __init__(self,ip,port,user=None,pwd=None):
        self._client= MongoClient(host=ip,port=port)
        if(user != None):
            self._client.admin.authenticate(user,pwd,mechanism='SCRAM-SHA-1')
        self._db= None
        self._collection= None

    def setDb(self,db):
        self._db= self._client[db]

    def setCollection(self,collection):
        self._collection= self._db[collection]

    def insert(self,data):
        self._collection.insert(data)

    def insert_Many(self,datalist):
        self._collection.insert_many(datalist)

    def find(self,fdata):
        result= self._collection.find(fdata)
        return result

    def find_one(self,fdata):
        result = self._collection.find_one(fdata)
        return result

    def update_one(self,fdata,updata):
        result= self._collection.update_one(fdata,updata)
        return result

    def update_many(self,fdata,updata):
        result= self._collection.update_many(fdata,updata)
        return result

#删除符合条件的所有数据
    def remove(self,fdata):
        return self._collection.remove(fdata)

    def delete_one(self):
        pass

    def delete_many(self):
        pass

if __name__ == '__main__':
    client = MongoConnector(CONFIG.MONGO_IP,CONFIG.MONGO_PORT)
    client.setDb('test')
    client.setCollection('col1')
    client.insert({'id':1,'name':'myname'})
    # client.update({'id':1},{'child':[{'idx':11,"name":'n11'},{"idx":12,"name":"n12"},{"idx":13,"name":"n13"}]})
    client.update_one({'id': 1},{'$set',
                  {'child':
                       {'a':
                            {'idx': 11, "name": 'n11'}, 'b':{"idx": 112, "name": "n12"}, 'c':{"idx": 113, "name": "n13"}
                        },
                   'nn':123
                   }})


'''
mongo方法：
db.getCollection('col1').find({'child.a.idx':11})
db.getCollection('col1').find({'id':123,'child.a.idx':11})   #与关系查询
db.getCollection('col1').update_many({'nn':123},{'$addToSet':{'added':1234546578}})  #集合中增加数组元素(到最外层)
db.getCollection('col1').update_many({'nn':123},{'$addToSet':{'child.a.added':1234546578}})  #集合中增加数组元素(到内层)
db.getCollection('col1').update({'child.id':11},{'$set':{'child.$.age':100}}) #数组内全部对象元素添加内容（child为数组，使用$占位）
#########################
# 以 $ 开头
$set # 更新/添加字段
$unset # 删除字段
$inc  # 自增  {$inc: {money: 10}} | 自减 {$inc: {money: -10}}
$exists # 是否存在
$in # 是否在...范围
$and
$or
$push  # 向数组中尾部添加一个元素（数组）
$addToSet # 向集合中添加元素（数组）
$pop  # 删除数组中的头部或尾部元素
$pull #删除所有满足条件值
'''