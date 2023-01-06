from math import sqrt
def checkprime
def findprimeFactor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp


print("enter two number:")
a=int(input())

print(findprimeGCD(a,b))
##INPUT
##enter two number:
##12
##15
##OUTPUT
##3
