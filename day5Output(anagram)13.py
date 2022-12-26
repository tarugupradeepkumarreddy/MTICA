def isanagrm(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'Yes'
    return 'No'
inp=input("enter strings:").split()
print(isanagrm(inp[0],inp[1]))
