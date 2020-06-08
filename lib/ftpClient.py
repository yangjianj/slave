# -*- coding: utf-8 -*-
import os
from ftplib import FTP
import config
class FtpClient():
    def __init__(self,host=config.FTPSERVER,user=config.FTP_USERNAME,passwd=config.FTP_PASSWORD):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.client = FTP(host=host,user=user,passwd=passwd)
    
    def upload(self,file,localfile):
        # file: uitest_base/suite_names/output.xml
        # localfile: tmp/test.txt
        fp = open(localfile,'rb')
        self.client.storbinary('STOR %s'%(file), fp)
        fp.close()
        print('upload succeed !')
        return True
    
    def download(self,filelist,localdir='../tmp/'):
        # file: uitest_base/suite_names/output.xml
        for file in filelist:
            if(not self.server_path_exist(file)):
                return None
            dirname,filename = os.path.split(file)
            dst_dir = os.path.join(localdir,dirname)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            try:
                fd = open(os.path.join(localdir,file),'wb')
                self.client.retrbinary('RETR %s'%(file),fd.write)
                print('download succeed !')
            except Exception as e:
                print('error:')
                print(e)
                print('download {0} failed!'.format(file))
            finally:
                fd.close()
        return True
    
    def delete(self,file):
        self.client.delete(file)
    
    def close(self):
        self.client.close()

    def dir(self,path=None):
        if path == None:
            path = self.client.pwd()
        if not self.server_path_exist(path):
            return None
        file_list = []
        print('dir:',path)
        self.client.dir(path,file_list.append)
        return file_list

    def server_path_exist(self,path):
        try:
            self.client.dir(path)
            return True
        except Exception as e:
            print(path,' not exist!')
            return False


    def mkd(self,pathname):
        try:
            self.client.mkd(pathname)
        except Exception as e:
            print(e)
        return True

    def pwd(self):
        return self.client.pwd()

if __name__ == '__main__':
    #ftp = FTP(host="127.0.0.1",user=  "test",passwd="123456")
    client = FtpClient()
    root_list = client.dir('suit1/suit1.py')
    for item in root_list:
        print(1111)
        print(item)
        dirname = item.split('\s+')
        dirname = list(filter(None,item.split(' ')))
        print(dirname)
    #client.delete('uitest_base/log.html')
    #client.mkd('test/test1/test2')
    #print(client.path_exist('test/test1'))
    # client.download(['sonar-scanner-cli-4.2.0.1873-windows.zip'])
    #client.upload('uitest_base/suite_names/output_up.xml','../tmp/redis_connector1.py')
    client.close()