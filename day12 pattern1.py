def printseries_num(p):
 if p>0:
    for i in range(1,p+1):
     num=1
     print()
     for j in range(i):
         print(num,end=' ')
         num+=1
 else:
    print('INVALID')
       
p=int(input('e.n:'))
printseries_num(p)
