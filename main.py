import random
startgame = input("Druk op enter om te beginnen.")

wordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" ,"heesterperk"]

print("Het spel is begonnen!")
x = (random.choice(wordlist))
y = len(x)
beurten = 5
print(x)
print ("Het woord heeft", ( y ) , "letters")

streepjes = ("_ ") * (y)
print (streepjes)
print ("U heeft", beurten, "beurten")

def gameGoed():
  









def in_voer():
  s = input()
  for char in s:
      if char.isalpha():
        if len(s)  != 1: 
          print("Maar 1 letter per keer graag")
          in_voer()
          break
        else: 
          print("Letter", ( s ), "ingevoerd")
          if s in x:
            print("Die letter is goed")
            gameGoed()
          else:
            print("fout")
            gameFout()
      else: 
        print("Vul een letter in")
        in_voer()
        break
in_voer()

w = input()
for w in x:
		if w != x:
			print("fout")
			break
		else:
			print("goed")
			break