import pathlib
import random
from string import ascii_letters


LISTARECI = pathlib.Path("lista_reci.txt") #ucitava listu
reci = [
    rec.upper() #forsira uppercase
    for rec in LISTARECI.read_text(encoding="utf-8").split("\n")
    if len(rec) == 5 and all(slovo in ascii_letters for slovo in rec) #filtriranje
]
rec = random.choice(reci) #nasumicno bira rec
for br_pog in range (1, 7):
    Pogodi = input("\nGuess a word:").upper()
    if Pogodi == rec:
        print("Correct")
        break
    #provera tacnosti
    tacna_slova = {slovo for slovo, tacno in zip(Pogodi, rec) if slovo == tacno}
    slova_van_mesta = set(Pogodi) & set(rec) - tacna_slova
    pogresna = set(Pogodi) - set(rec)
    
    print("Correct letters:", ", ".join((tacna_slova)))
    print("Misplaced letters:", ", ".join((slova_van_mesta)))
    print("Wrong letters:", ", ".join((pogresna)))
else:
    print("\nThe word was", rec)