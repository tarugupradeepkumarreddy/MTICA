def interchange3and5(n):
    n=str(n)
    n=n.replace('3','5')
    n=n.replace('5','3')
    n=n.replace('.','3')
    return n
a=int(input())
print(interchange3and5(a))
