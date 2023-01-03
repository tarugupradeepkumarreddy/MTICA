def printseries_num(p):
 for i in range(0,p,1):     
        print('.'*(p-i-1)+'*'*(i*2+1)+'.'*(p-i-1)) 
p=int(input('e.n:'))
printseries_num(p)
