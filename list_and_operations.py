#creating list
books=["english","science","maths","Art"]
print (books)

#Number of items
print(len(books))

#Retriving value indexing
print(books[1])

#retrive last title
print(books[len(books)-1])

#Add title
books.append("PE")
print(books)

#retieve all the item
for i in range(0,len(books)):
  print(books[i])
  
for i in books:
  print(i)
#Remove item
delete=input("Which item do you want to remove?")
if delete in books:
  books.remove(delete)
  print(books)
else:
  print("Sorry that is not in the list.")
  
#index is position in note (starting with 0)
#update or replace item
replace=input("Which item do you want to replace?")
keep=input("What/who do you want to replace it with?")
if replace in books:
  books[books.index(replace)]= keep
  print(books)
else:
  print("Sorry that is not in the list.")
