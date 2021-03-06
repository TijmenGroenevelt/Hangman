import random

def woordkiezen(): #functie die te raden woord terug geeft
  wordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" ,"heesterperk"]
  woord = (random.choice(wordlist))
  print ("Het woord heeft", len(woord) , "letters.")
  streepjes = ("_ ") * len(woord) #geeft  "_ _ _ _ _ _ _ "
  print (streepjes + "\n\n")
  return woord, streepjes

def nog_een_keer(): #boolean functie om opnieuw te spelen
  invalide_keuze = True
  while invalide_keuze: #checken of input correct is (ja of nee)
    keuze = input("Nog een keer spelen? (ja/nee): ")
    keuze = keuze.lower()
    if keuze not in ["ja", "nee"]:
      print("Voer correcte input in (ja/nee)")
    else:
      invalide_keuze = False

  if keuze.lower() == "ja":
    return True #opnieuw spelen
  else:
    return False #niet opnieuw spelen

def weergeven_woord(geraden_letter, woord, streepjes, lijst_foute_letters): #functie om letter in woord weer te geven + foutieve letters
  print("Lijst van foute letters: ", sorted(lijst_foute_letters))
  #print(woord)
  index = 0
  locaties_letter = [] #lijst met plekken
  for letter in woord: #loop over letters in woord
    if geraden_letter.lower() == letter:
      locaties_letter.append(index) #sla locatie op
    index = index + 1
  for locatie in locaties_letter: #loop over locaties in woord
    locatie_streepjes = locatie * 2 #*2 door spaties in streepjes string
    streepjes = streepjes[:locatie_streepjes] + geraden_letter.lower() + streepjes[locatie_streepjes+1:]
  return streepjes
  
def input_letter(geraden_letter_lijst, beurten): #vraag letter aan speler
  incorrect = True
  while incorrect: #loop die doorgaat tot 1 nieuwe letter is gegeven
    letter_input = input("Voer een letter in: ")
    if len(letter_input) == 0:
      print("Voer minimaal 1 letter in.")
      incorrect = True
      beurten = beurten - 1
      geef_beurten_weer(beurten)
    elif len(letter_input) > 1: 
      print("Maar 1 letter per keer graag.")
      incorrect = True
      beurten = beurten - 1
      geef_beurten_weer(beurten)
    elif not letter_input.isalpha():
      print("Input is geen letter, voer 1 LETTER in.")
      incorrect = True
      beurten = beurten - 1
      geef_beurten_weer(beurten)
    elif letter_input in geraden_letter_lijst: #voor dubbele letter geen beurt er af
      print("Letter is al gebruikt.")
      incorrect = True
    else:
      incorrect = False #1 letter gegeven
      geraden_letter_lijst.append(letter_input)
    if beurten == 0: #te veel fouten
      break
    
  return letter_input, geraden_letter_lijst, beurten

def check_letter_woord(geraden_letter, woord, lijst_foute_letters):
  print("Letter", geraden_letter, "ingevoerd.") #boolean functie, in woord of niet
  if geraden_letter.lower() in woord:
    print("Die letter is goed.")  
    goed_of_fout = True
  else:
    print("Die letter is fout.")
    goed_of_fout = False
    lijst_foute_letters.append(geraden_letter.lower()) #bijhouden foute letters
  return goed_of_fout, lijst_foute_letters

def geef_beurten_weer(beurten):
  if beurten == 1:
    print("U heeft nog maar 1 beurt!")
  else:
    print("U heeft nog", beurten, "beurten.")

  print(galg_plaatjes[beurten])
    
#Hier begint het spel, na alle functies
startgame = input("Druk op enter om te beginnen.")
print("Het spel is begonnen!")
spelen = True
beurten = 5
galg_plaatjes = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
galg_plaatjes.reverse() #omdraaien voor beurten getal

while spelen:
  woord, streepjes = woordkiezen()
  lijst_foute_letters = []
  geraden_letter_lijst = []
  while beurten != 0:
    geraden_letter, geraden_letter_lijst, beurten = input_letter(geraden_letter_lijst, beurten)
    
    if beurten != 0: #check of beurten 0 zijn na invalide invoer
      goed_of_fout, lijst_foute_letters = check_letter_woord(geraden_letter, woord, lijst_foute_letters)
      if not goed_of_fout: #False is niet in woord
        beurten = beurten - 1
        geef_beurten_weer(beurten)

    if beurten != 0: #check of beurten 0 zijn na foute letter
      streepjes = weergeven_woord(geraden_letter, woord, streepjes, lijst_foute_letters)
      print(streepjes + "\n\n")
    else:
      print("Beurten zijn op! Game over!!")
      print("Het woord was:", woord)

    if "_" not in streepjes: #check hele woord geraden
      print("Woord geraden! Gefeliciteerd!!")
      break
      
  spelen = nog_een_keer()
  if spelen:
    beurten = 5
print("Einde spel.")