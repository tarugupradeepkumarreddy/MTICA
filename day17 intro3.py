import sys
print("coming through stdout")
save_stdout=sys.stdout
print('sys.sysout:',sys.stdout)
fh=open(r"C:\Users\User\Desktop\pythonpractice43\day17\pkr.txt","w")
sys.stdout=fh
print("this line goes to pkr.txt")
print(input())
sys.stdout=save_stdout
fh.close()
