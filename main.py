import random
startgame = input("Druk op enter om te beginnen.")

wordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" ,"heesterperk"]

print("Het spel is begonnen!")
x = len(random.choice(wordlist))
beurten = 5

print ("Het woord heeft", ( x ) , "letters")

streepjes = ("_ ") * (x)
print (streepjes)
print ("U heeft", beurten, "beurten")

letters = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"


s = input()
for char in s:
    if char.isalpha():
      if len(s)  != 1: 
        print("Maar 1 letter per keer :)")
      else: 
        print("dit is nog niet af maar de les is afgelopen")
    else: 
      print("nietwaar")