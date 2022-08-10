
import webbrowser 
import re
import urllib.request

def Connection():
    try:
        urllib. request. urlopen("https://www.wikipedia.org/",timeout=5) #Python 3.x
        return True
    except Exception as E:
        print("Error is:",E)
        return False
        
def CheckURL_FromFile(path):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,path)      
    return [x[0] for x in url]
  
def Display(file_name):
    fd=open(file_name,'r')
    UrlList=CheckURL_FromFile(fd.read())
    
    for url in UrlList:
        webbrowser.open(url, new=2)



def main():
    print("___Marvellous Inofsystem____")
    
    print("Process Moniter")
    
    Data=input("Enter FilePath:")
    
    if Connection():
        Display(Data)
    else:
        print("Check Internet Connection")
     
        
if __name__=="__main__":
    main()