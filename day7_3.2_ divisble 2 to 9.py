ans=[ ]
for i in range(100,111):
    temp=[]
    for j in range(1,10):
       if i%j==0:
           temp.append(j)
    ans.append([i, max(temp)])
print(ans)

##ans={ i  for i in range(1,101) for j in range(2,10)  if i%j==0}
##print(*ans)
##print{ i  for i in range(1,101) for j in range(2,10)  if i%j==0}
##
