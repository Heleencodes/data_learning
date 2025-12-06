while True:
    naam = input('Wat is je naam?: ')
    
    if naam.lower() == 'stop':
        break
    
    if naam.lower() == 'heleen':
        print("Welkom terug, Heleen")
    else:
        print(f'Welkom, {naam}!')
    
    print(f'Jouw naam heeft {len(naam)} letters')

print("Tot de volgende keer!")




    