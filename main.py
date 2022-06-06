import random

def woordkiezen(): #functie die te raden woord terug geeft
  wordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" ,"heesterperk"]
  woord = (random.choice(wordlist))
  print ("Het woord heeft", len(woord) , "letters")
  streepjes = ("_ ") * len(woord) # "_ _ _ _ _ _ _ "
  return woord, streepjes

def nog_een_keer(): #functie om opnieuw te spelen
  #keuze = input("Nog een keer spelen? (Ja/Nee): ")
  #checken of input correct is
  #if ja/JA/Ja:
  #return True
  #else:
  return True

def weergeven_woord(geraden_letter, woord, streepjes, lijst_foute_letters): #functie om letter in woord weer te geven + foutieve letters
  print("Foute letters: ", lijst_foute_letters)
  print(woord)
  index = 0
  locaties_letter = [] #lijst met plekken
  for letter in woord:
    if geraden_letter.lower() == letter:
      locaties_letter.append(index)
    index = index + 1

  print(locaties_letter)
  for locatie in locaties_letter:
    locatie_streepjes = locatie * 2 #door spaties in streepje
    #print("locatie in streepjes", locatie_streepjes)
    streepjes = streepjes[:locatie_streepjes] + geraden_letter + streepjes[locatie_streepjes+1:]
  
  print(streepjes)
  return streepjes
  

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

def check_letter_woord(geraden_letter, woord, lijst_foute_letters):
  print("Letter", ( geraden_letter ), "ingevoerd")
  if geraden_letter.lower() in woord:
    print("Die letter is goed")  
    goed_of_fout = True
  else:
    print("Die letter is fout")
    goed_of_fout = False
    lijst_foute_letters.append(geraden_letter.lower())
  return goed_of_fout, lijst_foute_letters


#Hier begint het spel, na alle functies
startgame = input("Druk op enter om te beginnen.")
print("Het spel is begonnen!")
spelen = True
beurten = 5
while spelen:
  woord, streepjes = woordkiezen()
  lijst_foute_letters = []
  while beurten != 0:
    geraden_letter = input_letter()
    goed_of_fout, lijst_foute_letters = check_letter_woord(geraden_letter, woord, lijst_foute_letters)
    streepjes = weergeven_woord(geraden_letter, woord, streepjes, lijst_foute_letters)
    if not goed_of_fout: #False is fout
      beurten = beurten - 1
    
  #check hele woord geraden
  #check nog genoeg beurten
  spelen = nog_een_keer()
  if spelen:
    beurten = 5