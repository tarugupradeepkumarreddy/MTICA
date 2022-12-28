def add_five(x):
    temp=x+5
    return temp
num=[11,22,33,44,55]
result=list(map(lambda x:x+5,num))
result=list(map(add_five,num))
print(num)
print(result)
print('-'*40)
result=[i+5 for i in num]
print(result)
