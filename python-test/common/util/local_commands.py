#coding=utf-8
'''
Created on 2015年5月22日

@author: Puppy
'''
import os
import commands
class LocalCommands(object):
    '''
    exec local command
    '''
    
    def noReturnCommand(self,command):
        
        if command and not command.isspace():
            os.system(command)
            
        
    def getCommandOutPut(self,command):
        
        if command and not command.isspace():
            data=commands.getoutput(command)
            return data
            
    def getCommandStatusOutPut(self,command):        
        
        if command and not command.isspace():
            data=commands.getstatusoutput(command)
            return data
          
    def getOutPut(self,command,mode="r+"):
        
        if command and not command.isspace():
            lines=os.popen(command,mode).readlines()
            return lines
          

    def __init__(self):
        '''
        Constructor
        '''
if __name__ == '__main__':
    lc=LocalCommands()  
    lc.getOutPut('ls /')    
    
    