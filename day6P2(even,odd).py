lst=[]
lst_even=[]
lst_odd=[]
while(True):
    inp=int(input("enter a value(-1 to end):"))
    if inp==-1:
        break
    if inp%2==0:
       lst_even.append(inp)
    else:
        lst_odd.append(inp)
lst.sort()
print("lst_even",*lst_even)
print("min :",min(lst_even))
print("max :",(lst_even))
print("avg :",round(sum(lst_even)/len(lst_even),1))

print("lst_odd:" ,*lst_odd)
print("max :",lst_odd)
print("min :",lst_odd)
print("avg :",round(sum(lst_odd)/len(lst_odd),1))

