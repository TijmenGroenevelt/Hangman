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
  print("Foute letters: ", sorted(lijst_foute_letters))
  print(woord)
  index = 0
  locaties_letter = [] #lijst met plekken
  for letter in woord:
    if geraden_letter.lower() == letter:
      locaties_letter.append(index)
    index = index + 1
  for locatie in locaties_letter:
    locatie_streepjes = locatie * 2 #door spaties in streepje
    streepjes = streepjes[:locatie_streepjes] + geraden_letter.lower() + streepjes[locatie_streepjes+1:]
  return streepjes
  
def input_letter(geraden_letter_lijst):
  incorrect = True
  print(geraden_letter_lijst)
  while incorrect:
    letter_input = input("Voer een letter in: ")
    if len(letter_input) == 0:
      print("Voer 1 letter in.")
      incorrect = True
    elif len(letter_input) > 1: 
      print("Maar 1 letter per keer graag.")
      incorrect = True
    elif not letter_input.isalpha():
      print("Input is geen letter, voer 1 LETTER in.")
      incorrect = True
    elif letter_input in geraden_letter_lijst:
      print("Letter is al gebruikt.")
      incorrect = True
    else:
      incorrect = False
      geraden_letter_lijst.append(letter_input)
  return letter_input, geraden_letter_lijst

def check_letter_woord(geraden_letter, woord, lijst_foute_letters):
  print("Letter", ( geraden_letter ), "ingevoerd.")
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
  geraden_letter_lijst = []
  while beurten != 0:
    geraden_letter, geraden_letter_lijst = input_letter(geraden_letter_lijst)
    goed_of_fout, lijst_foute_letters = check_letter_woord(geraden_letter, woord, lijst_foute_letters)
    if not goed_of_fout: #False is fout
      beurten = beurten - 1
      if beurten == 1:
        print("U heeft nog maar 1 beurt!")
      else:
        print("U heeft nog", beurten, "beurten.")

    if beurten != 0:
      streepjes = weergeven_woord(geraden_letter, woord, streepjes, lijst_foute_letters)
      print(streepjes + "\n\n")
    else:
      print("Beurten zijn op! Game over!!")

    if "_" not in streepjes:
      print("Woord geraden! Gefeliciteerd!!")
  #check hele woord geraden
  spelen = nog_een_keer()
  if spelen:
    beurten = 5