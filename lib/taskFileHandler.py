# -*- coding: utf-8 -*-
import os
from mysqlConnector import DataManager
from ftpClient import FtpClient
import config as CONFIG

'''
in:caseid_list=['aacase1','index','aauitest2',]
out:组装成最终格式[{'suite':eee,'suitefile':suitenamepath,'cases':[eee,222,333]},{...}]

'''

_db = DataManager()
_ftpclient = FtpClient()

#数据库脚本路径转为ftp server脚本路径
def replace_casepath(caselist):
    result =[]
    for item in caselist:
        result.append(item.replace('$base$',''))
    return result

#case任务列表转为suite -- case信息表
def convert_task_to_download_list(tasklist):
    result=[]
    for item in tasklist:
        sql_obj= _db.exec_by_sql('select path from case_path where caseid="{0}"'.format(item))
        print(item)
        row = sql_obj.fetchone()  #not fetchall()
        if  row== None:
            print('not found caseid: ',item)  #log
            continue
        casepath = row
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

#下载suite--case列表对应的文件
def download_task_script(download_list,basedir=CONFIG.LOCAL_CASE_PATH):
    for task in download_list:
        #download suitfile
        suitfilepath = replace_casepath([task['suitefile']])
        print(suitfilepath)
        _ftpclient.download(suitfilepath,basedir)
        #download casefile
        casepath = replace_casepath(task['cases'])
        _ftpclient.download(casepath,basedir)
        #download config file
        suitpath= os.path.dirname(task['suitefile'])
        suitpath= replace_casepath([suitpath])[0]
        configpath= os.path.join(suitpath,'config')
        ftp_download_tree_file(configpath,basedir)

#config目录内文件下载
def ftp_download_tree_file(tree,basedir=CONFIG.LOCAL_CASE_PATH):
    dirlist= _ftpclient.dir(tree)
    print(dirlist)
    for item in dirlist:
        filename = list(filter(None, item.split(' ')))[-1]
        if item[0] == 'd':
            ftp_download_tree_file(os.path.join(tree,filename))
        else:
            _ftpclient.download([os.path.join(tree,filename)],basedir)

def download_tasklist(tasklist,dstdir=CONFIG.LOCAL_CASE_PATH):
    re = convert_task_to_download_list(tasklist)
    download_task_script(re,dstdir)

if __name__ == '__main__':
    tasklist=['aacase1','index','aauitest2',]
    download_tasklist(tasklist)