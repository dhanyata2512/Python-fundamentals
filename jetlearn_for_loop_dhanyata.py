#Print the numbers from 1 till the number entered by the user.
number = int(input("What numer would you like to end with?"))
for i in range (1,number+1,1):
  print(i)

#Print the odd numbers from 1 till the number entered by the user.
for i in range(1,number+1,2):
  print(i,end=" ")
  
  #Print multiplication table of a number.
times=int(input("What multiplication table do you want?"))
for i in range (1,11):
  print(times*i)

#Display the pattern:
#|
#| |
#| | |
#| | | |
#| | | | |

for i in range (1,11):
  print ("-"*i)

#Display reverse pattern:
#- - - - -
#- - - -
#- - -
#- -
#-

for i in range (10,0,-1):
  print("-"*i)
#Add all the numbers from 1 to a given number.
number=int(input("What number do you want?"))
total=0
for i in range (number+1):
  total=i+total
  print(total)
