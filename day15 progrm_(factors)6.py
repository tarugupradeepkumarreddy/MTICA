def findFactor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp
n=int(input())
print(*findFactor(n))
 
##INPUT
##30
##OUTPUT
##1 2 3 5 6 10 15 30
