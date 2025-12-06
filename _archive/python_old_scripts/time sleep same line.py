"""
leeftijd_validator.py

Robuust console-script dat:
- valideert of de gebruiker een numerieke leeftijd invoert
- bij meerdere (onlogische) pogingen vraagt om geboortejaar
- na meerdere mislukte pogingen verwijst naar contact (functie klaar om link te openen)
- overzichtelijke functies zodat dit makkelijk in een GUI/webapp hergebruikt kan worden
"""

import datetime
import webbrowser
from typing import Tuple, Optional

CONTACT_URL = "https://www.jouwbedrijf.nl/contact"  # pas aan naar echte URL


def validate_age_input(text: str) -> Tuple[bool, Optional[int], str]:
    """
    Probeer tekst naar een geldige leeftijd (int) te converteren.
    Returns: (is_valid, leeftijd_of_None, foutmelding)
    """
    s = text.strip()
    if not s:
        return False, None, "Leeg invoer"
    # eventueel accepteren van '50\n' etc. int() pakt dat
    try:
        age = int(s)
    except ValueError:
        return False, None, "Geen geldig getal"
    if age < 0:
        return False, None, "Leeftijd kan geen negatief getal zijn"
    return True, age, ""


def calculate_age_from_birthyear(year: int, current_year: Optional[int] = None) -> int:
    """Bereken leeftijd op basis van geboortejaar."""
    if current_year is None:
        current_year = datetime.datetime.now().year
    return current_year - year


def contact_opnemen(open_browser: bool = False, url: str = CONTACT_URL) -> None:
    """Laat contactinformatie zien; optioneel: open de link in de browser (standaard False)."""
    print("\nNeem a.u.b. contact op met onze klantenservice:")
    print(f"→ {url}")
    if open_browser:
        try:
            webbrowser.open(url)
            print("(De browser is geopend)")
        except Exception as e:
            print(f"(Kon de browser niet openen: {e})")


def main(max_pogingen: int = 4) -> None:
    """
    Hoofdlogica:
    - accepteer maximaal max_pogingen (standaard 4)
    - na 3 onsuccesvolle pogingen vraag geboortejaar
    - bij 4e mislukte poging: contactoptie tonen
    """
    pogingen = 0
    huidig_jaar = datetime.datetime.now().year

    while True:
        invoer = input("Hoe oud ben je? (of typ 'q' om te stoppen) ").strip()

        # snelle exit-optie
        if invoer.lower() in {"q", "quit", "exit"}:
            print("Uitstappen. Tot ziens!")
            return

        geldig, leeftijd, fout = validate_age_input(invoer)

        if geldig:
            # leeftijd is een int
            assert isinstance(leeftijd, int)
            if leeftijd < 100:
                print("Je bent oud genoeg om mee te doen! Eigenlijk ben je nu U")
                # hier kun je extra logica toevoegen (bv. leeftijdsgebonden bericht)
                return
            else:
                print("Dat lijkt me sterk, probeer opnieuw.")
                pogingen += 1
        else:
            # ongeldige invoer (niet-numeriek, leeg, negatief)
            print(f"Fout: {fout}. Probeer het opnieuw (voer een getal in).")
            pogingen += 1

        # Na 3 onsuccesvolle pogingen: vraag geboortejaar
        if pogingen == 3:
            invoer_jaar = input("Voer dan je geboortejaar in (bijv. 1990): ").strip()
            if invoer_jaar.isdigit():
                geboortejaar = int(invoer_jaar)
                leeftijd = calculate_age_from_birthyear(geboortejaar, huidig_jaar)
                if 0 < leeftijd < 100:
                    print(f"Dat klinkt logischer. Je bent ongeveer {leeftijd} jaar oud!")
                    print("Je bent oud genoeg om mee te doen! Eigenlijk ben je nu U")
                    return
                else:
                    print("Hmm, dat klopt nog steeds niet helemaal. Laten we niet verder gaan.")
                    return
            else:
                print("Dat is geen geldig geboortejaar. Probeer het later nog eens.")

        # Als het aantal pogingen het maximum bereikt
        if pogingen >= max_pogingen:
            # laatst: contactoptie
            contact_opnemen(open_browser=False)
            return


if __name__ == "__main__":
    main()
