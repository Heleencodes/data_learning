bewerking = input("Wat wil je doen? (optellen, aftrekken, vermenigvuldigen, delen): ")

getal1 = int(input("Eerste getal: "))
getal2 = int(input("Tweede getal: "))

if bewerking == "optellen":
    resultaat = getal1 + getal2
elif bewerking == "aftrekken":
    resultaat = getal1 - getal2
elif bewerking == "vermenigvuldigen":
    resultaat = getal1 * getal2
elif bewerking == "delen":
    resultaat = getal1 / getal2
else:
    resultaat = "Onbekende bewerking!"

print(f"Het resultaat is: {resultaat, 3}")