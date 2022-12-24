import math
def  primenumber(n):
    if n<1:
        return 0
    if n==1 or n==2 or n==3:
        return n
    count=int(math.sqrt(n)+1)
    for i in range(2,count):
        if n%i==0:
           return 0
    return n
strat=int(input())
stop=int(input())
lst=[]
for i in range(strat,stop+1):
    if primenumber(i):
        lst.append(i)
print(*lst)
print(len(lst))
   
