Boodschappen = ["Appels", "Peren", "Bananen", "Kersen"]

while True:
    nieuwe_boodschap = input("Wat wil je toevoegen aan de boodschappenlijst? (of typ 'klaar' om te stoppen) ")
    if nieuwe_boodschap.lower() == 'klaar':
        break

    # normaliseer invoer (maak eerste letter hoofdletter)
    nieuwe_boodschap = nieuwe_boodschap.strip().capitalize()

    # check of het item al in de lijst staat (ongeacht hoofdletters)
    if nieuwe_boodschap.lower() in [b.lower() for b in Boodschappen]:
        print(f"{nieuwe_boodschap} staat al op de lijst!")
    else:
        Boodschappen.append(nieuwe_boodschap)
        print(f"{nieuwe_boodschap} toegevoegd aan de lijst.")

# alfabetisch sorteren
Boodschappen.sort()

print("\nJe boodschappenlijst:")
for item in Boodschappen:
    print("-", item)