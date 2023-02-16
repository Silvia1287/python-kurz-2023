cislo = input("Zadaj číslo: ")
def over_cislo (cislo):
    if len(cislo) == 9:
        sms = input("Text sms: ")
    elif len(cislo) == 13 and cislo[0:3]== "+420":
        sms = input("Text sms: ")
    return sms

over_cislo()

