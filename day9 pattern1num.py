def printseries_num(n):
    for  i in range (1,n+1):
        for j  in range(1,i):
            print(i, end=' ')
        print(i)
    print('-'*10)
    for  i in range (1,n+1):
        for j  in range(1,i+1):
            print(j, end=' ')
        print()
    print('-'*10)
    num=1
    for i in range (1,n+1):
        print()
        for j  in range(i):
            print(num, end=' ')
            num+=1
    
       
       

n=int(input('e.n:'))
printseries_num(n)
