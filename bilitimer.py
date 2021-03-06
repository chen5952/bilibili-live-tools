import asyncio
import time
import Tasks
import printer


def CurrentTime():
    currenttime = int(time.time())
    return currenttime


class BiliTimer:
    __slots__ = ('jobs', 'loop')
    instance = None

    def __new__(cls, loop=None):
        if not cls.instance:
            cls.instance = super(BiliTimer, cls).__new__(cls)
            cls.instance.loop = loop
            Tasks.init()
        return cls.instance
    
    def excute_async(self, i):
        print('执行', i)
        asyncio.ensure_future(i[0](*i[1]))
      
    @staticmethod
    def call_after(func, delay):
        inst = BiliTimer.instance
        value = (func, ())
        inst.loop.call_later(delay, inst.excute_async, value)
        # print('添加任务', time_expected, func.__name__, func, tuple_values)
        # print('添加任务')
        return
        
    @staticmethod
    def append2list_jobs(func, time_expected, tuple_values):
        inst = BiliTimer.instance
        current_time = CurrentTime()
        value = (func, tuple_values)
        inst.loop.call_later(time_expected-current_time, inst.excute_async, value)
        # print('添加任务', time_expected, func.__name__, func, tuple_values)
        return
        
    @staticmethod
    def getresult():
        print('数目', BiliTimer.instance.jobs.qsize())
        
    
