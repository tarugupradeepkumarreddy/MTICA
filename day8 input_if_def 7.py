def EvenOdd(num):
    assert(num>0),"Negitive numbers"
    if num%2==1:
        return "even"
    else:
        return "Odd"
for i in range(3):
    num=int(input("e.n:"))
    try:
       print(num, 'is',EvenOdd(num))
    except AssertionError as ob:
        print(ob)

