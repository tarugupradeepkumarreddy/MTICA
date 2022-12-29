def div(a,b):
    assert (isinstance(a,int) or isinstance(a,float)),\
            'first Argument should be either integer or float'
    assert( isinstance(b,int) or isinstance(b,float)) ,\
            'second Argument should be either integer or float'
    assert (b!=0),"Division by zero is not defined"
    return a/b

try:
    print(div(55,0))
except AssertionError as ob:
    print(ob)
try:
    print(div(20,3))
except AssertionError as ob:
    print(ob)
try:
    print(div(100,20))
except AssertionError as ob:
    print(ob)
try:
    print(div('hello',20))
except AssertionError as ob:
    print(ob)
try:
    print(div('hell',20))
except AssertionError as ob:
    print(ob)
