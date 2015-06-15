#coding=utf-8

'''
Created on 2015年5月22日

@author: Puppy
'''
from _io import open


class ReadFile(object):
    '''
    classdocs
    '''
    def readFileContent(self,file_name,read_op="r+"):
        
        
        with open(file_name,read_op) as f:
        
            lines=f.readlines()
           
            return lines
            

    def __init__(self):
        '''
        Constructor
        '''
 
      
if __name__ == '__main__':
        
            
    read_file = ReadFile();
    lines=read_file.readFileContent("H:\\test.txt")
    for line in lines:
        print line
                
            
           
            
            