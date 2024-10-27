#Write a program for a calculator. User should be able to enter first value then the operator (+,-,*,/) for the operation they want to perform and then the second value. Based on the selected operation and input values, the result should be displayed. The user should be able to perform as many calculations as they like until they select the option to stop.
print("Hi this is a calculator!")
while True:
  number1=int(input("What would you like your first number to be:"))
  operation=(input("What operation would you like to use:"))
  number2=int(input("What would you like the second number to be:"))
  if operation == "+":
    print(number1 + number2)
  elif operation == "-":
    print(number1 - number2)
  elif operation == "*":
    print(number1 * number2)
  elif operation == "/":
    print(number1 / number2)  
  else:
    print("sorry i dont know that one") 
  
  stop = input("Say yes if you want to stop and no if you don't:")
  if stop == "yes":
    break 

  
