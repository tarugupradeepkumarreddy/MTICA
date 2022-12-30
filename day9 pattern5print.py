def printseries_num(n):        
    print('-'*10)
    num=1
    for i in range (1,n+1):
        print()
        for j  in range(i):
            print(num, end=' ')
            num+=1
n=int(input('e.n:'))
printseries_num(n)
