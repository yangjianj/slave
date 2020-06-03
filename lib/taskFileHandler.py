# -*- coding: utf-8 -*-
import os
from mysqlConnector import DataManager
from ftpClient import FtpClient
import config as CONFIG

'''
组装成最终格式[{'suite':eee,'suitefile':suitenamepath,'cases':[eee,222,333]},{...}]

'''

_db = DataManager()
_ftpclient = FtpClient()

def replace_casepath(caselist):
    result =[]
    for item in caselist:
        result.append(item.replace('$base$',''))
    return result

def convert_task_to_download_list(tasklist):
    result=[]
    for item in tasklist:
        sql_obj= _db.exec_by_sql('select path from case_path where caseid="{0}"'.format(item))
        for casepath in sql_obj.fetchall():
            suite_dir= casepath[0].split("\\")[-2]
            suitefile= os.path.join(os.path.dirname(casepath[0]),suite_dir+'.py')
            saved = False
            for i in range(len(result)):
                if result[i]['suite'] == suite_dir:
                    result[i]['cases'].append(casepath[0])
                    saved = True
            if saved == False:
                result.append({'suite':suite_dir,'suitefile':suitefile,'cases':[casepath[0]]})
    return result

def download_task_script(download_list):
    for task in download_list:
        #download suitfile
        suitfilepath = replace_casepath([task['suitefile']])
        print(suitfilepath)
        _ftpclient.download(suitfilepath,CONFIG.LOCAL_CASE_PATH)
        #download casefile
        casepath = replace_casepath(task['cases'])
        _ftpclient.download(casepath,CONFIG.LOCAL_CASE_PATH)
        #download config file
        suitpath= os.path.dirname(task['suitefile'])
        configpath= os.path.join(suitpath,'config')
        ftp_download_tree_file(configpath)

def ftp_download_tree_file(tree):
    dirlist= _ftpclient.dir(tree)
    for item in dirlist:
        filename = list(filter(None, item.split(' ')))[-1]
        if item[0] == 'd':
            ftp_download_tree_file(os.path.join(tree,filename))
        else:
            _ftpclient.download([os.path.join(tree,filename)],CONFIG.LOCAL_CASE_PATH)






tasklist=['casefile','index']
re= convert_task_to_download_list(tasklist)
print(re)
download_task_script(re)