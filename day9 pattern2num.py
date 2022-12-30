def printseries_num(n):
    for  i in range (1,n+1):
        for j  in range(1,i):
            print(i, end=' ')
        print(i)
    print('-'*10)
        
n=int(input('e.n:'))
printseries_num(n)
