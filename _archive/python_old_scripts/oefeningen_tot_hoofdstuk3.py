# ================================================
# OEFENINGEN AUTOMATE THE BORING STUFF (t/m H3)
# ================================================

# ----------------------
# Hoofdstuk 1 – Intro
# ----------------------

print("Hello, World!")
print("What is your name?")
name = input("Heleena: ")
print("It is good to meet you, " + name)
print("The length of your name is:")
print(len(name))


# ----------------------
# Hoofdstuk 2 – If/Else & Booleans
# ----------------------

name = "Helen"
if name == "Helen":
    print("Welkom terug!")
else:
    print("Wie ben jij?")


# ----------------------
# Hoofdstuk 3 – Loops
# ----------------------

# Aftellen
for i in range(10, 0, -1):
    print(i)
print("Start!")

# Continue voorbeeld
for i in range(5):
    if i == 2:
        continue
    print(i)

# Tafelscript
multiplier = int(input("Welke wil je zien: "))
start = 1
end = 10
while start <= end:
    result = start * multiplier
    print(f"{start} x {multiplier} = {result}")
    start += 1

# If + tafel gecombineerd
print("What is your name?")
name = input()
if name == "Alice":
    print("Speciale toegang.")
else:
    print("Welkom, " + name)

multiplier = int(input("Welke tafel wil je zien?: "))
for i in range(1, 11):
    print(f"{i} x {multiplier} = {i * multiplier}")


# ----------------------
# Extra Oefeningen – For vs While
# ----------------------

# Oefening 1 – 1 t/m 5 printen
for i in range(1, 6):
    print(i)

# Oefening 2 – Vraag naam tot ‘stop’
while True:
    name = input("What is your name? ").strip()
    if name.lower() == "stop":
        break

# Oefening 3 – Hallo 10x
for _ in range(10):
    print("Hallo!")

# Oefening 4 – Terug tellen
for i in range(20, -1, -1):
    print(i)
print("BOEM!")

# Oefening 5 – Wachtwoord-check (basisversie)
while True:
    wachtwoord = input("Wat is het wachtwoord? ")
    if wachtwoord == "python":
        print("Toegang verleend")
        break

# Oefening 5 – Wachtwoord-check (clean code versie)
MAX_POGINGEN = 3
pogingen = 0
correct_wachtwoord = "python"

while pogingen < MAX_POGINGEN:
    invoer = input("Wat is het wachtwoord? ").strip().lower()
    if invoer == correct_wachtwoord:
        print("✅ Toegang verleend")
        break
    else:
        pogingen += 1
        print(f"❌ Fout wachtwoord, poging {pogingen} van {MAX_POGINGEN}")

if pogingen == MAX_POGINGEN:
    print("🚫 Toegang geweigerd. Te veel pogingen.")
