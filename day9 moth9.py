def printMoth(n,dn):
    
    if n<=12:
        return[dn]
    else:
       return'Invaild'
n=int(input())
dic={1:'January',2:'Feb',3:'March',4:'April',5:'May',6:'June'
     ,7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec' }
print(printMoth(n,dn))
