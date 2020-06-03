# -*- coding: utf-8 -*-
import sys,os
import time
import logging
from watchdog.events import *
from watchdog.observers import Observer
from mysqlConnector import DataManager
import config as CONFIG
'''
使用限制：
1.拷贝（新建）时源目录只能有一个根目录，否则不能完全识别到新增文件
2.仅完成新建文件同步到数据库，后续完善
'''
_db = DataManager()

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        #FileSystemEventHandler.__init__(self)
        super().__init__()

    def on_moved(self, event):
        if event.is_directory:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),": directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"： file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"： directory created:{0}".format(event.src_path))
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"： file created:{0}".format(event.src_path))
            update(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"： directory deleted:{0}".format(event.src_path))
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"： file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"： directory modified:{0}".format(event.src_path))
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),"： file modified:{0}".format(event.src_path))



class MonitorDir():
    def __init__(self):
        self.event_handler= [FileEventHandler(),]
        self.observer = Observer()

    def startMonitor(self,dir):
        watch= self.observer.schedule(self.event_handler[0], dir, True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("===error===")
            self.observer.stop()
        self.observer.join()

def update(srcpath,dstpath=None):
    path = srcpath.replace(CONFIG.MONITOR_BASEDIR, '$base$')
    filename = os.path.basename(srcpath)
    caseid= filename.split('.')[0]
    _db.exec_by_sql('insert into case_path(caseid,casename,path) values("{0}","{1}","{2}")'.format(caseid,filename,path))

if __name__ == "__main__":
    s= MonitorDir()
    s.startMonitor(CONFIG.MONITOR_BASEDIR)
    '''
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "e:/tmp", True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
'''
