def fact(n):
    assert (n>=0),"factoral of negative number is not defined !"
    assert(isinstance(n,int)),"factoral floating point number is not defined !"
    if  n==0:
        return 1
    else:
        return n*fact(n-1)

    
try:
    print (fact(-45))
except Exception as ob:
    print(ob)
try:
    print (fact(45))
except Exception as ob:
    print(ob)
try:
    print (fact(4.9))
except Exception as ob:
    print(ob)
try:
    print (fact('today'))
except Exception as ob:
    print(ob)
print("thank you")

