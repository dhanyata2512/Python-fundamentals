import random 
randon_number=random.randint(1,20)
while True:
  guess=int(input("What number am I thinking of?"))
  if guess<randon_number:
    print("Your guess is low.")
  elif guess==randon_number:
    print ("You are right!")
    break
  else:
    print("Your guess is high.")

print(randon_number)
