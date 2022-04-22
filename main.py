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
