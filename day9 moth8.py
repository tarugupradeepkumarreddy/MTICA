def printMoth(dn):
    if (dn==1):
        return 'january'
    elif(dn==2):
        return 'February'
    elif(dn==3):
        return 'March'
    elif(dn==4):
        return 'April'
    elif(dn==5):
        return 'May'
    elif(dn==6):
        return 'june'
    elif(dn==7):
        return 'July'
    elif(dn==8):
        return 'Augest'
    elif(dn==9):
        return 'September'
    elif(dn==10):
        return 'October'
    
    elif(dn==11):
        return 'November'    
    
    elif(dn==12):
        return 'Deceamber'
    else:
        return'Invaild'
num=int(input())
print(printMoth(num))
    
