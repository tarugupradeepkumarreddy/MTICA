def printseries_num(n):
    for  i in range (1,n+1):
        for j  in range(1,i+1):
            print(j, end=' ')
        print()
n=int(input('e.n:'))
printseries_num(n)


