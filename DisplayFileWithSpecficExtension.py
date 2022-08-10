#1.Design automation script which accept directory name and file extension from user. Display all 
#files with that extension. 
#Usage : DirectoryFileSearch.py “Demo” “.txt” 
#Demo is name of directory and .txt is the extension that we want to search.


#steps :
#1. find files in directory and print files from dir
#2. find extension of every file
#3. accept dir name 
#4. compare extension 
#5. create log file( write file with given extension in that file )

from sys import *
import os
import pathlib

Data=dict()
def Dictonary(Key ,Value):
    global Data
    Data[Key]=Value
 
def CompareExt(fileext):
    fd=open("log_table.txt","a")
    fd.write("{} files are :\n".format(fileext))
    global Data
    for keys in Data:
        if(Data[keys] == fileext):
            fd.write(keys)
            fd.write("\n")
            
    
def Display(path,ext):
    path=os.path.abspath(path)
    isFile = os.path.isdir(path)
    if(isFile==False):
        print("Dir is not Exist")
        
    for root, dirs, files in os.walk(path):    
        for filename in files:
            file_extension = pathlib.Path(filename).suffix
            Dictonary(filename,file_extension)
            
    CompareExt(ext)
                
           
def main():
    print("-----Shreyas Narsale: Automation1 ----")
    print("Script Name:",argv[0])
    
    if((len(argv) >3 ) and (len(argv) < 2)):
        print("Invalid Number of parameter")
        print("Enter -U flaf for Usage")
        print("Enter -H flag for Help")
        exit()
        
    if(len(argv)==2):
        if ( argv[1]=="-u" )or (argv[1]=="-U"):
            print("Usage : script which accept directory name and file extension from user. Display all files with that extension. ")
            exit()
        
        if ( argv[1]=="-h" )or (argv[1]=="-H"):
            print("Help : Name_of_Script   Path_of_file   Extension")
            print("Path_of_file: Enter Valid path")
            print("Extension: (ex.= .txt)")
            exit()
            
    if(len(argv)==3):
        try:
            Display(argv[1],argv[2])
            print("Done!!!")
            print("Check Log table ")
        
        except Exception :
            print("Exception while excuting the script")
            print("Please Check input , contact developer")

        


if __name__=="__main__":
    main()