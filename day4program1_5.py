def checkArmstrongnumber(n):
    n=str(n)
    total=0
    for i in n:
        total+=int(i)**len(n)
    if int(n)==total:
        return 1
    return 0
inp=int(input())
if checkArmstrongnumber(inp):
    print ("YES")
else:
    print("NO")
   
