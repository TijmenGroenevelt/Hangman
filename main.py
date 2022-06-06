import random

def woordkiezen(): #functie die te raden woord terug geeft
  wordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" ,"heesterperk"]
  woord = (random.choice(wordlist))
# y = len(x)
# print ("Het woord heeft", ( y ) , "letters")
# streepjes = ("_ ") * (y)
# print (streepjes)
  # aantal streepjes ook returnen
  return woord

def nog_een_keer(): #functie om opnieuw te spelen
  #keuze = input("Nog een keer spelen? (Ja/Nee): ")
  #checken of input correct is
  #if ja/JA/Ja:
  #return True
  #else:
  return False

def gameGoed(): #functie om letter in woord weer te geven
  pass
def gameFout(): 
  pass

def input_letter():
  incorrect = True
  while incorrect:
    input_letter = input("Voer een letter in: ")
    if len(input_letter) == 0:
      print("Voer 1 letter in")
      incorrect = True
    elif len(input_letter) > 1: 
      print("Maar 1 letter per keer graag")
      incorrect = True
    elif not input_letter.isalpha():
      print("Input is geen letter, voer 1 LETTER in")
      incorrect = True
    else:
      incorrect = False
  return input_letter

def check_letter_woord(input_letter):
  print("Letter", ( input_letter ), "ingevoerd")
  if input_letter in woord:
    print("Die letter is goed")
    gameGoed()
  else:
    print("fout")
    gameFout()

#Hier begint het spel, na alle functies
startgame = input("Druk op enter om te beginnen.")
print("Het spel is begonnen!")
spelen = True
while spelen:
  te_raden_woord = woordkiezen()
  geraden_letter = input_letter()
  
  #het hele spel
  spelen = nog_een_keer()  