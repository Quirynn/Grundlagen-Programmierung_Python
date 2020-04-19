from nutzer import Nutzer

vorname = input("Vorname:")
nachname = input("Nachname:")
ersterNutzer = Nutzer(vorname, nachname)

print(ersterNutzer.getVorname())
print(ersterNutzer.getNachname())
