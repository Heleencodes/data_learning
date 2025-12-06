while True:
    naam = input('Wat is je naam?: ')
    
    if naam == 'stop':
        break
    
    if naam == 'Heleen':
        print(f'Welkom terug, {naam}!')
    else:
        print(f'Welkom, {naam}!')
    
    print(f'Jouw naam heeft {len(naam)} letters')

print("Tot de volgende keer!")