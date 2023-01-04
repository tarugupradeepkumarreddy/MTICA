def printSunday():
    print('Sunday')
    return
def printMonday():
    print('Monday')
def printTuesday():
    print(' Tuesday')
def printWednesday():
    print('Wednesday')
def printThrusday():
    print(' Thrusday')
def printFrinday():
    print(' Frinday')
def printSaturday():
    print(' Saturday')
def printQuit():
    print(' Quit')    
def choice():
    print("enter day number between 1-7")
##    print("1:Sunday")
##    print("2:Monday")
##    print("3:Tuesday")
##    print("4:Wednesday")
##    print("5:Thrusday")
##    print("6:Frinday")
##    print("7:Saturday")
##    print("8:Quit")
##    return
dayDict={1:printSunday,2:printMonday,3:printTuesday, 4:printWednesday,5:printThrusday,6:printFrinday,7:printSaturday,8:printQuit}
dayNo=int(input())
if dayNo>=1 and day<=8:
    dayDict[dayNo]
else:
    print("Invalid")
##selection=0
##while True:
##    if selection>=8:break
##    choice()
##    selection=int(input("selction day option:"))
##    if (selection>=1)and  (selection<=8):
##       dayDict[selection]()
##
