Boodschappen = ["Appels", "Peren", "Bananen", "Kersen"]

while True:
    nieuwe_boodschap = input("Wat wil je toevoegen aan de boodschappenlijst? (of typ 'klaar' om te stoppen) ")
    if nieuwe_boodschap.lower() == 'klaar':
        break
    Boodschappen.append(nieuwe_boodschap)

print("\nJe boodschappenlijst:")
for item in Boodschappen:
    print("-", item)
    