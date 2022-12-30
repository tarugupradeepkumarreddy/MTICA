def printMoth(dn):
    mn=''
    if (dn==1):
        mn= 'january'
    elif(dn==2):
        mn= 'February'
    elif(dn==3):
        mn= 'March'
    elif(dn==4):
        mn= 'April'
    elif(dn==5):
       mn='May'
    elif(dn==6):
        mn='june'
    elif(dn==7):
        mn= 'July'
    elif(dn==8):
        mn= 'Augest'
    elif(dn==9):
        mn= 'September'
    elif(dn==10):
       mn='October' 
    
    elif(dn==11):
        mn= 'November'    
    
    elif(dn==12):
        mn= 'Deceamber'
    else:
        mn='not vaild'
    return mn
def printMoth(dn):
    mn=''
    if (dn==1):
        mn= 'january'
    elif(dn==2):
        mn= 'February'
    elif(dn==3):
        mn= 'March'
    elif(dn==4):
        mn= 'April'
    elif(dn==5):
       mn='May'
    elif(dn==6):
        mn='june'
    elif(dn==7):
        mn= 'July'
    elif(dn==8):
        mn= 'Augest'
    elif(dn==9):
        mn= 'September'
    elif(dn==10):
       mn='October' 
    
    elif(dn==11):
        mn= 'November'    
    
    elif(dn==12):
        mn= 'Deceamber'
    else:
        mn='not vaild'
    return mn
import time
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(printMoth(inpNum))
    print((time.time()-start)*10000000)
    start=time.time()
    print(printMoth(inpNum))
    print((time.time()-start)*10000000) 
    
