#3. Design automation script which accept directory name from user and create log file in that 
#directory which contains information of running processes as its name, PID, Username. 

import datetime
import psutil
import os
from sys import *

def LogFile(ListProc,src_path):
    now=datetime.datetime.now()
    date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
    FileName="logFile_"+date_time+".txt"
    
    src_path=os.path.abspath(src_path)
    
    isFile = os.path.isdir(src_path)
    if(isFile==False):
        print("Dir is not Exist")
        print("Path is not valid")
        exit()
        
    file_name=os.path.join(src_path,FileName)
    
    fd=open(file_name,"a")
    date_time = now.strftime("Date :%m/%d/%Y , Time: %H:%M ")
    Data="information of running processes :("+date_time+")\n"
    fd.write(Data)
    Data=("_________________________________________________________\n")
    fd.write(Data)
    iCnt=1
    for Process_info in ListProc:
        #print(Process_info)
        Data=("Process No.:"+str(iCnt)+"\n")
        fd.write(Data)
        Data=("Process id:"+str(Process_info[0])+"\n")
        fd.write(Data)
        Data=("process Name:"+Process_info[1]+"\n")
        fd.write(Data)
        Data=("process Username:"+Process_info[2]+"\n")
        fd.write(Data)
        Data=("__________\n")
        fd.write(Data)  
        iCnt+=1
        
    Data=("_________________________________________________________\n")
    fd.write(Data)
    
def ProcessDisplay(Path):
    listprocess=[]
    for proc in psutil.process_iter():#to travl process (in psutil.process_iter)
        try:
            pinfo=[proc.pid,proc.name(),proc.username()]
            listprocess.append(pinfo)
            
                
                
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass #errors
    
    #print(listprocess)
    LogFile(listprocess,Path)       
    


def main():
    print("-----Shreyas Narsale: Automation1 ----")
    print("Script Name:Process Moniter")
    
    
    if((len(argv) >2)or (len(argv) <2)):
        print("Invalid Number of parameter")
        print("Enter -U flaf for Usage")
        print("Enter -H flag for Help")
        exit()
        
    if(len(argv)==2):
        if ( argv[1]=="-u" )or (argv[1]=="-U"):
            print("Usage : which accept directory name from user and create log file in that ") 
            print("directory which contains information of running processes as its name, PID, Username. ")
            exit()
        
        if ( argv[1]=="-h" )or (argv[1]=="-H"):
            print("Help : Name_of_Script  LogFilePath")
            print("LogFilePath: Enter Valid Path")
            exit()
            
        
    try:
        ProcessDisplay(argv[1])
        print("Done!!!")
        
    except Exception as E :
        print("Exception while excuting the script",E)
        print("Enter Valid Process name")
        print("Please Check input , contact developer")

        


if __name__=="__main__":
    main()