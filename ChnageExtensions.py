#2. Design automation script which accept directory name and two file extensions from user. 
#Rename all files with first file extension with the second file extenntion. 
#Usage : DirectoryRename.py “Demo” “.txt” “.doc”

#steps:
#1. find files in directory and print files from dir
#2. find extension and  compare extension and rename file
#3. create log file( write chnaged data  )
from sys import *
import os
            
    
def logFile(oldfile,newfile):
    fd=open("logFile.txt","a")
    fd.write("Following Changes are Done in your Dir:\n")
    Data=("Old File is:  "+oldfile)
    fd.write(Data)
    fd.write("\n")
    Data=("Rename File is: "+newfile)
    fd.write(Data)
    fd.write("\n")
    
def Display(path,Given_Ext,Changing_Ext):
    path=os.path.abspath(path)
    isFile = os.path.isdir(path)
    if(isFile==True):
        print("Dir Exist")
    else:
        print("Dir is not Exist")
    
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            Exact_File=os.path.basename(path)
            file_name, file_extension = os.path.splitext(path)
            if(file_extension==Given_Ext):
                New_file=file_name+Changing_Ext
                logFile(path,New_file)
                os.rename(path,New_file)
                
                
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
            print("Usage : script which accept directory name and two file extensions from user.") 
            print("Rename all files with first file extension with the second file extenntion. ")
            exit()
        
        if ( argv[1]=="-h" )or (argv[1]=="-H"):
            print("Help : Name_of_Script   Path_of_file   First_Extension Second_Extension")
            print("Path_of_file: Enter Valid path")
            print("First_Extension: File Extension")
            print("Second_Extension: Changing Extension")
            exit()
            
    if(len(argv)==4):
        try:
            Display(argv[1],argv[2], argv[3])
            print("Done!!!")
            print("Check Given Dir ")
        
        except Exception :
            print("Exception while excuting the script")
            print("Please Check input , contact developer")

        


if __name__=="__main__":
    main()