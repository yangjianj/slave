# -*- coding: utf-8 -*-
import sys
import time
import logging
from watchdog.events import *
from watchdog.observers import Observer

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
    def __init__(self,dir):
        self.monitor= dir
        self.event_handler= FileEventHandler()
        self.observer = Observer()

    def startMonitor(self):
        self.observer.schedule(self.event_handler, self.monitor, True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

if __name__ == "__main__":
    s= MonitorDir('e:/tmp')
    s.startMonitor()
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
