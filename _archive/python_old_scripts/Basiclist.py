namen = []
for i in range(3):  # herhaal 3 keer
    naam = input(f"Voer naam {i+1} in: ")
    namen.append(naam)
print(f"Er zijn {len(namen)} namen ingevoerd: {namen}")
print(f"Hallo {namen[0]}")
print(f"Hallo {namen[1]}")
print(f"Hallo {namen[2]}")