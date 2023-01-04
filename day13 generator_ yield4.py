def squares(x=0):
    while x<10:
        x=x+1
        yield x*x
##yieldedlist=[i for i in squares()]
##print(yieldedlist)
yieldedlist=list(squares())
print(yieldedlist)




















