##def day(dn):
##    if (dn==1):
##        return 'sunday'
##    elif(dn==2):
##        return 'Monday'
##    elif(dn==3):
##        return 'Tuesday'
##    elif(dn==4):
##        return 'Wednesday'
##    elif(dn==5):
##        return 'Thrusday'
##    elif(dn==6):
##        return 'Friday'
##    elif(dn==7):
##        return 'saturday'
##    else:
##        return'Invaild'
def day(dn):
    mn=''
    if (dn==1):
        mn='sunday'
    elif(dn==2):
        mn= 'Monday'
    elif(dn==3):
        mn='Tuesday'
    elif(dn==4):
        mn= 'Wednesday'
    elif(dn==5):
       mn= 'Thrusday'
    elif(dn==6):
        mn='Friday'
    elif(dn==7):
        mn= 'saturday'
    else:
        mn='not vaild'
    return mn
for i in range(3):
    num=int(input())
    print(day(num))
    
    

        
