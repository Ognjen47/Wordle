import pathlib
import random
from string import ascii_letters
from rich.console import Console # type: ignore
console = Console(width=70)

def obrisi(naslov): #brisemo sadrzaj ekrana nakon svakog pokusaja
    console.clear()
    console.rule(f"[bold blue] {naslov} [/]\n")

def random_rec():
    LISTARECI = pathlib.Path("lista_reci.txt")
    reci = [
        rec.upper() #forsira uppercase
        for rec in LISTARECI.read_text(encoding="utf-8").split("\n")
        if len(rec) == 5 and all(slovo in ascii_letters for slovo in rec) #filtriranje
    ]
    return random.choice(reci)

def proveri(pokusaji, rec):
    for pokusaj in pokusaji:
        styled_guess = []
        for slovo, tacno in zip(pokusaj, rec):
            if slovo == tacno:
                vizuelizacija = "bold white on green"
            elif slovo in rec:
                vizuelizacija = "bold white on yellow"
            elif slovo in ascii_letters:
                vizuelizacija = "white on #666666"
            else:
                vizuelizacija = "dim"
            styled_guess.append(f"[{vizuelizacija}]{slovo}[/]")

        console.print(" ".join(styled_guess), justify="center")
        
def kraj_igre(pokusaji, rec, tacno):
    obrisi(naslov= "Game Over") # type: ignore
    proveri(pokusaji, rec)
    
    if tacno:
        console.print(f"\n[bold white on green]Correct, the word is {rec}[/]")
    else:
        console.print(f"\n[bold white on red]Incorrect, the word was {rec}[/]")
        
def pogadjanje(prethodni_unos):
    pogodi=input("\nGuess a word: ").upper()
    
    if pogodi in prethodni_unos:
        print(f"You've already guessed {pogodi}.")
        return pogadjanje(prethodni_unos)
    
    if len(pogodi) != 5:
        print("Your guess must be 5 letters.")
        return pogadjanje(prethodni_unos)
    
    if any((invalid := slovo) not in ascii_letters for slovo in pogodi):
        print(f"Invalid letter: {invalid}.")
        return pogadjanje(prethodni_unos)
    
    return pogodi

def main():
    rec = random_rec()
    pokusaji=['_' * 5] * 6 #menjamo u listu kako bi smo pratili korisnicke pokusaje 
    for i in range (6):
        obrisi(naslov=f"Guess {i + 1}")
        proveri(pokusaji, rec)

        pokusaji[i] = pogadjanje(prethodni_unos=pokusaji[:i])

        if pokusaji[i]==rec:
            break

    kraj_igre(pokusaji, rec, tacno=pokusaji[i]==rec)

if __name__ == "__main__":
    main()