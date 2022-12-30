def prinseries(ch,n):
    assert isinstance(ch,str),'frist number should be string'
    assert isinstance(n,int),'second number should be string'
    for i in range(1,n+1,1):
        print(ch*i)
    print('-'*50)
    
    return None
inpch=input("enter a character:")
inpNum=int(input("enter a no:"))
try:
    prinseries(inpch,inpNum)
except AssertionError as a:
    print(a)






































