# opdracht 1 tpt en met 5 van paragraaf 2.6
# opdracht 1
postcode = "1234AB"
print(postcode.lower())
# opdracht 2
woonplaats = "Amstelveen"
print(woonplaats.upper())
# opdracht 3
verzendmethode = "PostNL"
betaalmethode = "iDEAL"
print(verzendmethode.lower())
print(betaalmethode.upper())
# opdracht 4
postcode = input("Wat is je postcode?")
print(postcode.upper())
# opdracht 5
woonplaats = input("Wat is je woonplaats?")
if len(woonplaats) == 1:
    print("Jou woonplaats heeft 1 teken")
else:
    print("Jou woonplaats heeft " + str(len(woonplaats)) + " tekens")