'''
Created on 2015年5月22日

@author: Administrator
'''

class LogOjbect(object):
    '''
    通用日志对象
    '''


    def __init__(self, dic):
        '''
        Constructor
        '''
        self.ip=dic['ip']
        self.log_date=dic['log_date']
        self.user_agnet=dic['user_agnet']