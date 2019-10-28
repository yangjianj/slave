# -*-coding:UTF-8 -*-
import sqlite3
import config

class DataManager():
    def __init__(self):
        dbpath= config.DATABASE
        self._conn = sqlite3.connect(dbpath,check_same_thread=False)
        self._cc = self._conn.cursor()

    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

    def exec_by_sql(self,sql):
        self._cc.execute(sql)
        self._conn.commit()
        return True

    def close_conn(self):
        self._conn.close()

    def query_users(self):
        table=self._cc.execute("select * from Users")
        self._conn.commit()
        return table

    def update_user(self,name,workid,role,project,telephone):
        try:
            table=self._cc.execute("update Users set workid='%s', role='%s',project='%s',telephone='%s'  \
            where name='%s'"%(workid,role,project,telephone,name))
            self._conn.commit()
            return True
        except Exception as e:
            print(e)
            return e

    def add_user(self,name,workid,role,project,telephone):
        pass

    def delete_user(self,name):
        pass

    def save_api_result(self,taskid,caseid,result,response,spend,starttime,endtime):
        try:
            sql = "update api_case_result set result ='%s' ,response = '%s',spend= '%s',starttime = '%s',endtime = '%s' where taskid = '%s' and caseid = '%s'"% (result,response,spend,starttime,endtime,taskid,caseid)
            #sql1 = "insert into api_case_result (caseid,version,api_link,request_data,response,result,spend,starttime,endtime) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(caseid,version,url,request_data,response,result,spend,start_time,end_time)
            print(sql)
            self._cc.execute(sql)
            self._conn.commit()
            return True
        except Exception as e:
            print("sql error----------------------")
            print(e)
            return e

    def save_ui_result(self,taskid,caseid,status,message,error,starttime,endtime):
        try:
            sql = "update ui_case_result set result = '%s',output = '%s',result_message = '%s',starttime = '%s',endtime = '%s' where taskid = '%s' and caseid = %s"% (status,message,error,starttime,endtime,taskid,caseid)
            #sql1 = "insert into ui_case_result (caseid,result,output,result_message,starttime,endtime) values('%s','%s','%s','%s','%s','%s')" % (case,status,message,error,starttime,endtime)
            self._cc.execute(sql)
            self._conn.commit()
            return True
        except Exception as e:
            print("sql error----------------------")
            print(e)
            return e




if __name__ == '__main__':
    dd=DataManager()
    re=dd.query_Users()
    for i in re:
        print(i)
