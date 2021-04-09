# -*- cording: utf-8 -*-

'''APP log record

@author: Gulinjie
@time: 2019-05-14
'''


import logging
import threading


class Log:
    def __init__(self):
        self.logger = logging.getLogger("[FusionSolar-Test]")
        self.logger.setLevel(logging.DEBUG)

        #ch = logging.StreamHandler()
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(format)
        self.logger.addHandler(ch)


class MyLog:
    lock = threading.RLock()
    log = None

    def __init__(self):
        pass

    @staticmethod
    def getLog():
        if MyLog.log is None:
            MyLog.lock.acquire()
            MyLog.log = Log()
            MyLog.lock.release()
        return MyLog.log


