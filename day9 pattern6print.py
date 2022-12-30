def printseries_num(n):
    for i in range(0,n,1):
        print('.'*(n-i-1)+'*'*(i*2+1)+'.'*(n-i-1))
n=int(input('e.n:'))
printseries_num(n)

    
        
