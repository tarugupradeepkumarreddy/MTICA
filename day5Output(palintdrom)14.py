def ispalindrome(p):
    if p==p[::-1]:
       return 'Yes'
    return 'No'
inp=input("enter strings:")
print(ispalindrome(inp))
