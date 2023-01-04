def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMult(a,b):
    return a*b
def printDiv(a,b):
    return a/b
def choice():
    print("+:Addition")
    print("-:Substraction")
    print("*:multication")
    print("/:division")
    print("q:Quit")
    return
pradeep={"+":printAdd,"-":printSub,"*":printMult,"/":printDiv}
while True:
    choice()
    selection=input("selection an arithmetic operation:")
    if selection=='q' or selection=='Q':break
    if ((selection=="+") or(selection=="-")or
        (selection=="*") or (selection=="/")):
        n1=int(input())
        n2=int(input())
        z=pradeep[selection](n1,n2)
        print(n1,selection,n2,"=",z)
