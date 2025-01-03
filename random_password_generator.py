#Random Password Generator. The password should consists of 2 digits, 2 capital letters, 2 small letters and 2 special characters chosen randomly.

import random

number1=random.randint(0,9)
number2= random.randint(0,9)
sletters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cletters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
spcl_chars = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","|","<",">"]

s1=random.choice(sletters)
s2=random.choice(sletters)
c1=random.choice(cletters)
c2=random.choice(cletters)
sc1=random.choice(spcl_chars)
sc2=random.choice(spcl_chars)

password=[s1,s2,c1,c2,sc1,sc2,str(number1),str(number2)]
print(password)
random.shuffle (password)
print(password)
word= "".join(password)
print(word)
