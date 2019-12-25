# -*-coding:UTF-8 -*-
import os
from lib.ftp_client import FtpClient
import config

class Uicase():
    def __init__(self):
        pass
    
    def download_case(self,task):
        #下载uicase
        ftpclient = FtpClient(config.UI_CASE_FTPSERVER,config.UI_FTP_USERNAME,config.UI_FTP_PASSWORD)
        pathlist = self.serach_case_ftppath(task)
        casedir = os.path.join(config.UICASE_DIR,task.product+task.version+task.id)
        ftpclient.download(pathlist,casedir)
        return casedir
    
    def serach_case_ftppath(self,caselist):
        #寻找uicase路径并返回
        for i in caselist:
            pass
    
