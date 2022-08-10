#4. Design automation script which accept two directory names and one file extension. Copy all 
#files with the specified extension from first directory into second directory. Second directory 
#should be created at run time. 
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe” 
#Demo is name of directory which is existing and contains files in it. We have to create new 
#Directory as Temp and copy all files with extension .exe from Demo to Temp.

#1. create a new Directory in parent directory
#2. comapre specified extension
#3. copy that extension file from one to create directory
#4.save in logFile



from sys import *
import os
import shutil

def logFile(Created_Dir_Name,Copy_File_Name):
    fd=open("logFile.txt","a")
    fd.write("Following Changes are Done in your Dir:\n")
    Data=("CreateDir is:  "+Created_Dir_Name)
    fd.write(Data)
    fd.write("\n")
    Data=("Copy_File_Name File is: "+Copy_File_Name)
    fd.write(Data)
    fd.write("\n")
    
def CreateDir(path,FileName):
    PrarentDir=os.path.abspath(os.path.join(path, os.pardir))#gives path of parent dir
    New_dir = os.path.join(PrarentDir, FileName)
    os.mkdir(New_dir) 
    return New_dir
    
def Display(path,NewDir,Ext):
    path=os.path.abspath(path)
    isFile = os.path.isdir(path)
    if(isFile==False):
        print("Dir is not Exist")
        
    dest=CreateDir(path,NewDir)
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            File_Path = os.path.join(root, filename)
            Exact_File=os.path.basename(File_Path)
            file_name, file_extension = os.path.splitext(File_Path)
            if(file_extension==Ext):
                try:
                    logFile(dest,File_Path)
                    shutil.copy(File_Path, dest)
                except Exception as E:
                    print("File is already Exist")
                    print("Error Occured :",E)
                
                
           
                
def main():
    print("-----Shreyas Narsale: Automation1 ----")
    print("Script Name:",argv[0])
    
    if((len(argv) >4 ) or (len(argv) < 2)):
        print("Invalid Number of parameter")
        print("Enter -U flaf for Usage")
        print("Enter -H flag for Help")
        exit()
        
    if(len(argv)==2):
        if ( argv[1]=="-u" )or (argv[1]=="-U"):
            print("Usage : script which accept two directory names and one file extension. Copy all ")
            print("files with the specified extension from first directory into second directory.") 
            exit()
        
        if ( argv[1]=="-h" )or (argv[1]=="-H"):
            print("Help : Name_of_Script   Path_of_Src_Directory   Desinatin_Dir_Name   File_Extension")
            print("Path_of_Src_Directory: Enter Valid path of Source Dir")
            print("Desinatin_Dir_Name: Only Write Name of Desinatin_Dir")
            print("File_Extension: Enter Extension of copy files")
            exit()
            
    if(len(argv)==4):
        try:
            Display(argv[1],argv[2],argv[3])
            print("Done!!!")
            print("Check Given Dir ")
        
        except Exception as E :
            print("Exception while excuting the script",E)
            print("Please Check input , contact developer")

        


if __name__=="__main__":
    main()