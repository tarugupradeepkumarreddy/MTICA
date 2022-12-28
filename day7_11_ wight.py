dict1={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bicycle":7,"motorcycle":110}
##ls=[]
##for i in dict1:
##    if dict1[i]<5000:
##       ls.append(i.upper())
####       ls.append(i.lower())
##      
##print(ls)
##ls=[i.upper() for i in dict1 if dict1[i]<5000]
##print(ls)
print([i.upper() for i in dict1 if dict1[i]<5000])
