def prinseriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def prinseriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpch=input("enter a character:")
inpNum=int(input("enter a no:"))
prinseriesIncreasing(inpch,inpNum)
print('-'*40)
prinseriesDecreasing(inpch,inpNum)
