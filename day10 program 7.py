pp=open(r'C:\Users\User\Desktop\pythonpractice43\day10\day10.txt',"r")
pp1=open(r'C:\Users\User\Desktop\pythonpractice43\day10\test.txt',"w+")
temp=pp.read()
pp1.write(temp)
pp.close()
pp1.close()
print("File copied")
























