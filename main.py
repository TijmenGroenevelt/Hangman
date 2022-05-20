import random
startgame = input("Druk op enter om te beginnen.")

wordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" ,"heesterperk"]

print("Het spel is begonnen!")
x = (random.choice(wordlist))
y = len(x)
beurten = 5

print ("Het woord heeft", ( y ) , "letters")

streepjes = ("_ ") * (y)
print (streepjes)
print ("U heeft", beurten, "beurten")

s = input()
for char in s:
    if char.isalpha():
      if len(s)  != 1: 
        print("Maar 1 letter per keer graag") 
		  break
      else: 
        print("dit is nog niet af maar de les is afgelopen")
    else: 
      print("Vul een letter in")
		break