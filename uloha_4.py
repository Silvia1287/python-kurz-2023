import math
def over_cislo (cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and cislo[0:4]== "+420":
        return True
    else:
        return False

cislo = input("Zadaj telefónne číslo: ")
cislo_ok = over_cislo(cislo)

if cislo_ok == True:
    sms = input("Zadaj text sms: ")
    cena_sms= math.ceil(len(sms)/179) * 3
    print(f"Cena za sms správu je: {cena_sms}")
else:
    print("Číslo nie je správne.")
