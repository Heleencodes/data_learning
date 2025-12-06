import datetime

# Geboortedatum vragen
jaar = int(input("In welk jaar ben je geboren?: "))
maand = int(input("In welke maand (nummer) ben je geboren?: "))
dag = int(input("Op welke dag van de maand ben je geboren?: "))

# Datum maken
geboortedatum = datetime.date(jaar, maand, dag)

# Dag van de week ophalen
dag_van_week = geboortedatum.strftime("%A")

print(f"Je bent geboren op {dag_van_week}, {geboortedatum}")
print(f"Je bent geboren op {dag_van_week}, {geboortedatum}")
