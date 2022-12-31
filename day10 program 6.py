pp=open(r'C:\Users\User\Desktop\pythonpractice43\day10\day10.txt',"a")
for i in  range(5):
    inpstr=input("enter string:")
    pp.write(inpstr+'\n')
pp.close()
print("Written to file")
























inpstr=input('Enter text:')
gh.write(inpstr)
inpstr=input('enter text:')
gh.write(inpstr)
gh.close()
print('text written to file')
