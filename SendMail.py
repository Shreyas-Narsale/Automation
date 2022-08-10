import smtplib
import urllib.request
import socket

socket.getaddrinfo('192.168.137.1', 8080)
def Connection():
    try:
        urllib. request. urlopen("https://www.wikipedia.org/",timeout=5) #Python 3.x
        return True
    except Exception as E:
        print("Error is:",E)
        return False


def Mail():
    import smtplib
    socket.getaddrinfo('192.168.137.1', 8080)
    fromMy = 'shreeprac12@yahoo.com' # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
    to  = 'shreyasnarsale765@gmail.com'
    subj='TheSubject'
    date='2/1/2010'
    message_text='Hello Or any thing you want to send'

    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )

    username = str('shreeprac12@yahoo.com')  
    password = str('Shree@123')  

    try :
        server = smtplib.SMTP("smtp.mail.yahoo.com",587)
        server.connect("shreeprac12@yahoo.com",465)
        server.login(username,password)
        server.sendmail(fromMy, to,msg)
        server.quit()    
        print ('ok the email has sent ')
    except Exception as E :
        print( "Error Occured:",E)
        
        
def main():
    if Connection():
        print("Internet Connection")
        #Server_Connect()
        Mail()
    else:
        print("No Internet Connection")
        
    


if __name__=="__main__":
    main()