import datetime
ob=datetime.datetime.now()
print(type(ob))
print("-"*25)
print(ob)
print(ob.year)
print(ob.month)
print(ob.day)
print(ob.hour)
print(ob.minute)
print(ob.second)
str1=str(ob.hour)+':'+str(ob.minute)+':'+str(ob.second)
print(str1)
print("-"*25)
print("1 week ago it was:",ob -datetime.timedelta(weeks=1))
print("100 days ago it was :",ob -datetime.timedelta(days=100))
print("1 week from now it will be :",ob +datetime.timedelta(weeks=1))
print("1000 days later it will be :",ob +datetime.timedelta(days=100))
bday_prasad=datetime.datetime(1999,8,24)
print("-"*25)
print("Birthday in ...",ob-bday_prasad)
print("-"*25)
