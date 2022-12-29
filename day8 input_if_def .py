num1=int(input("e.n:"))
def Even(num1):
    str1=''
    if num1%2==0:
        str1=str(num1)+" is even"
    return str1
def Odd(num1):
    if num1%2==1:
        return "Odd"
num=int(input("e.n:"))
x=Even(num1)
y=Odd(num1)
print("x=",x)
print("y=",y)
print(Even(num1))
print(Odd(num1))
