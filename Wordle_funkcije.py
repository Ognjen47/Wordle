import pathlib
import random
from string import ascii_letters

def random_rec():
    LISTARECI = pathlib.Path("lista_reci.txt")
    reci = [
        rec.upper() #forsira uppercase
        for rec in LISTARECI.read_text(encoding="utf-8").split("\n")
        if len(rec) == 5 and all(slovo in ascii_letters for slovo in rec) #filtriranje
    ]
    return random.choice(reci)

def proveri(Pogodi, rec):
    tacna_slova = {slovo for slovo, tacno in zip(Pogodi, rec) if slovo == tacno}
    slova_van_mesta = set(Pogodi) & set(rec) - tacna_slova
    pogresna = set(Pogodi) - set(rec)
    
    print("Correct letters:", ", ".join((tacna_slova)))
    print("Misplaced letters:", ", ".join((slova_van_mesta)))
    print("Wrong letters:", ", ".join((pogresna)))

def main():
    rec = random_rec()
    br = 7
    for br_pog in range (1, 7):
        print("\nYou have ",br-1, "chances to guess the correct word.")
        Pogodi = input("\nGuess a word:").upper()

        
        proveri(Pogodi, rec)
        if Pogodi==rec:
            break
    else:
        print("\nThe word was", rec)

if __name__ == "__main__":
    main()