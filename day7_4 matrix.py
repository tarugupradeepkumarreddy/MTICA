m=[[1,2],[3,4],[5,6],[7,8]]
ans=[]
for row in range(len(m[0])):
    temp=[]
    for col in range(len(m[0])):
       temp.append(m[col][row])
    ans.append(temp)
print(ans)

##print([[m[row][col]for row in range(len(m[0]))]for col in range(len(m[0]))])     
##
##temp=[[m[row][col]for row in range(len(m[0]))] for col in range(len(m[0]))]
##print(temp)
