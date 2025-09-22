# opdrachten 1 tot en met 6 van paragraaf 2.9
# Vraag 1
totaalprijs = 50.00
kortingsBon = 10.00
nieuwePrijs = totaalprijs - kortingsBon
print("Nieuwe prijs na korting: " + str(nieuwePrijs) + " EUR.")

# Vraag 2
cijfer1 = 8.5
cijfer2 = 7.0
gemiddelde = (cijfer1 + cijfer2) / 2
print("Het gemiddelde van de cijfers is: " + str(gemiddelde))

# Vraag 3
prijsExclBtw = float(input("Voer het bedrag exclusief btw in: "))
prijsInclBtw = prijsExclBtw * 1.21
print("Bedrag inclusief 21% btw: " + str(prijsInclBtw) + " EUR.")

# Vraag 4
getal1 = int(input("Geef een getal: "))
getal2 = int(input("Geef nog een getal: "))
uitkomst = getal1 + getal2
print("De optelling van deze getallen is: " + str(uitkomst))

# Vraag 5
bedrag = float(input("Voer het bedrag in euro's in: "))
wisselkoers = 1.1648
bedragDollar = bedrag * wisselkoers
print("Het bedrag in Amerikaanse dollars is: " + str(bedragDollar))

# Vraag 6
totaalPrijs = float(input("Voer de totaalprijs in: "))
kortingsPercentage = float(input("Voer het kortingspercentage in: "))
totaalPrijsInclKorting = totaalPrijs * (1 - kortingsPercentage / 100)
print("Totaalprijs incl. korting: " + str(totaalPrijsInclKorting) + " EUR.")