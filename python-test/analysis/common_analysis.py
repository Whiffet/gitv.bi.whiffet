#coding=utf-8
'''
Created on 2015年5月22日

@author: puppy
'''

import log_content

class CommonAnalysis(object):
    '''
               解析Uri
    '''
    def analysisCommonParams(self,log,separator="|"):
        if log and not log.isspace():
            logList=log.split(separator)
            if len(logList)>=3:
                if len(logList)==4:
                    commonList=logList[0:2]+logList[3:4]
                    uri=logList[2]
                    return (commonList,uri)
                elif len(logList)==3:
                    commonList=logList[0:2]
                    uri=logList[2]
                    return (commonList,uri)
                
                   

    def __init__(self):
        '''
        Constructor
        '''
if __name__ == '__main__':
    ca=CommonAnalysis()
    log=ca.analysisCommonParams(log_content.LOG_CONTENT)
    print log[0]
    print log[1]