#Create a program that will allow the user to easily manage a list of names. 
#You should display a menu that will allow them to add a name to the list, change a name in the list, delete a name from the list or view all the names in the list. 
#There should also be a menu option to allow the user to end the program. 
#If they select an option that is not relevant, then it should display a suitable message. 
#After they have made a selection to either add a name, change a name, delete a name or view all the names, they should see the menu again without having to restart the program.
#Add a name
#Change a name
#Delete a name
#View all names
#Stop

#creating list 
list=[]

while True:
  change=input("1.Add a name \n 2.Change name \n 3.View all names \n 4.delete a name \n 5.Stop \n")
  
  if change == "1":
    Add= input ("Who do you want to add?")
    list.append(Add)
  elif change == "2":
    change=input("Who do you want to exchange?")
    new= input ("Who do you wanty to replace it with?")
    if change in list:
      list[list.index(change)]=new

  elif change == "3":
    print(list)
  elif change == "4":
    delete=input ("who do you want to remove?")
    if delete in list:
      list.remove(delete)
  
  elif change == "5":
    break
  else:
    print("sorry I don't know that")
