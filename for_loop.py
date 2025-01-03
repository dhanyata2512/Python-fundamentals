number = int(input("What number would you like?\n "))
for i in range(2,number+1,+2):
    print(i)

number1 = int(input("What number would you like?\n "))
for i in range(number1,0,-1):
    print(i)

#leap year
year = int(input("What year would you like?\n "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
    print("Leap year")
else:
   print("Not a leap year")
