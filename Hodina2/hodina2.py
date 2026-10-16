cislo = 0

while cislo < 10:
    if cislo == 7:
        cislo = cislo + 1
        continue
    else:
        print(cislo)
    cislo = cislo + 1


print()

from random import randint

while True:
    cislo = randint(1,100)
    print(cislo)
    if cislo == 4:
        break
