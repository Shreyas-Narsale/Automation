#3. Design automation script which accept two directory names. Copy all files from first directory 
#into second directory. Second directory should be created at run time. 
# Usage : DirectoryCopy.py Demo Temp
#steps:
#1.find Address Parent dir
#2. copy files form one Dir to another directory
#3.write changes in log table



from sys import *
import os
import shutil

def LogFile(Actual_File,Copyed_File):
    fd=open("logFile.txt","a")
    Data=("Actual file: {} \n ".format(Actual_File))
    fd.write(Data)
    Data=("Copyed file is: {} \n ".format(Copyed_File))
    fd.write(Data)

def CreateDir(path,FileName):
    PrarentDir=os.path.abspath(os.path.join(path, os.pardir))#gives path parent dir
    New_dir = os.path.join(PrarentDir, FileName)
    return New_dir
    
def CopyDir(src_path,New_Dir_Name):
    src_path=os.path.abspath(src_path)
    isFile = os.path.isdir(src_path)
    if(isFile==False):
        print("Dir is not Exist")
        print("Path is not valid")
        
    try:
        Dest_path=CreateDir(src_path,New_Dir_Name)
        dest=shutil.copytree(src_path, Dest_path) 
        LogFile(src_path,dest)
    except Exception as E:
        print("File is Already Exists")
        print("Error Occured:",E)
    
                
def main():
    print("-----Shreyas Narsale: Automation1 ----")
    print("Script Name:",argv[0])
    
    if((len(argv) >3 ) or (len(argv) < 2)):
        print("Invalid Number of parameter")
        print("Enter -U flaf for Usage")
        print("Enter -H flag for Help")
        exit()
        
    if(len(argv)==2):
        if ( argv[1]=="-u" )or (argv[1]=="-U"):
            print("Usage : script which accept two directory names. Copy all files from first directory") 
            print("into second directory.")
            exit()
        
        if ( argv[1]=="-h" )or (argv[1]=="-H"):
            print("Help : Name_of_Script   Path_of_Src_Directory   Desinatin_Dir_Name")
            print("Path_of_Src_Directory: Enter Valid path of Source Dir")
            print("Desinatin_Dir_Name: Only Write Name of Desinatin_Dir")
            exit()
            
    if(len(argv)==3):
        try:
            CopyDir(argv[1],argv[2])
            print("Done!!!")
            print("Check Given Dir ")
        
        except Exception as E :
            print("Exception while excuting the script",E)
            print("Please Check input , contact developer")

        


if __name__=="__main__":
    main()