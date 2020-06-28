# -*- coding: utf-8 -*-
import os
from lib.mysqlConnector import DataManager
from lib.ftpClient import FtpClient
import config as CONFIG

'''
in:caseid_list=['aacase1','index','aauitest2',]
out:组装成最终格式[{'suite':eee,'suitefile':suitenamepath,'cases':[eee,222,333]},{...}]

'''
class TaskFileHandler():
    def __init__(self):
        self._db = DataManager()
        self._ftpclient = FtpClient()
    #数据库脚本路径转为ftp server脚本路径
    def replace_casepath(self,caselist):
        result =[]
        for item in caselist:
            result.append(item.replace('$base$\\',''))
        return result

    #case任务列表转为suite -- case信息表
    def convert_task_to_download_list(self,tasklist):
        #将任务转组装成suite包含case的形式，并有suite case的文件路径
        result=[]
        for item in tasklist:
            sql_obj= self._db.exec_by_sql('select path from case_path where caseid="{0}"'.format(item))
            print(item)
            row = sql_obj.fetchone()  #not fetchall()
            if  row== None:
                print('not found caseid: ',item)  #log
                continue
            casepath = row
            suite_name= casepath[0].split("\\")[-2]
            suitefile= os.path.join(os.path.dirname(casepath[0]),suite_name+'.robot')
            saved = False
            for i in range(len(result)):
                if result[i]['suitefile'] == suitefile:
                    result[i]['cases'].append(casepath[0])
                    saved = True
            if saved == False:
                result.append({'suite':suite_name,'suitefile':suitefile,'cases':[casepath[0]]})
        return result

    #下载suite--case列表对应的文件
    def download_task_script(self,download_list,basedir=CONFIG.LOCAL_CASE_PATH):
        for task in download_list:
            #download suitfile
            suitfilepath = self.replace_casepath([task['suitefile']])
            self._ftpclient.download(suitfilepath,basedir)
            #download casefile
            casepath = self.replace_casepath(task['cases'])
            self._ftpclient.download(casepath,basedir)
            
            suitpath= os.path.dirname(task['suitefile'])
            suitpath= self.replace_casepath([suitpath])[0]
            #create __init__.py
            modulefile = os.path.join(basedir,suitpath,'__init__.py')
            fd = open(modulefile,'wb')
            fd.close()
            # download config file
            configpath= os.path.join(suitpath,'config')
            self.ftp_download_tree_file(configpath,basedir)
    
    #config目录内文件下载not exist
    def ftp_download_tree_file(self,tree,basedir=CONFIG.LOCAL_CASE_PATH):
        dirlist= self._ftpclient.dir(tree)
        if not dirlist:
            return None
        print(dirlist)
        for item in dirlist:
            filename = list(filter(None, item.split(' ')))[-1]
            if item[0] == 'd':
                self.ftp_download_tree_file(os.path.join(tree,filename))
            else:
                self._ftpclient.download([os.path.join(tree,filename)],basedir)
    
    def download_tasklist(self,tasklist,dstdir=CONFIG.LOCAL_CASE_PATH):
        re = self.convert_task_to_download_list(tasklist)
        self.download_task_script(re,dstdir)

if __name__ == '__main__':
    td = TaskFileHandler()
    tasklist=['aacase1','index','aauitest2',]
    td.download_tasklist(tasklist)