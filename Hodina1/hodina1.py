from random import randint

print("Zobudil si sa v tajomnej jeskyni!")
meno = input("Ako sa volas ? ")

print("Ahoj", meno)
print("Pred tebou su dvoje dvere.")
print("1 - Cervene dvere")
print("2 - Modre dvere")

volba = input("Cislo ktorych dveri otvoris ? ")

if volba == "1":
    print("Za dverami je DRAK!")
    nahoda = randint(0,9)
    if nahoda < 5:
        print("PORAZIL si draka.")
        print("Nasiel si poklad a vyhravas")
    else:
        print("Drak ta zjedol. KONIEC HRY.")
elif volba == "2":
    print("Nasiel si POKLAD!")
    print("VYHRAL SI!")
else:
    print("Neotvoril si ziadne dvere")
