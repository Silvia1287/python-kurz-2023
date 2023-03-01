#\d\d?\.\d\d?\.\d\d\d\d
#\d\d?\. ?\d\d?\. ?\d\d\d\d
#\d\d?\W\d\d?\W\d\d\d\d
#\d{3} ?\d{2}..?[a-zA-Z]

import re

regularny_vyraz = re.compile(r"[a-zA-Z]{6,10}")

meno = input("Zadaj svoje meno: ")

vstup_ok = regularny_vyraz.fullmatch(meno)
if vstup_ok:
    print("OK")
else:
    print("Nesprávné meno") 

regularny_vyraz = re.compile(r"\w*(\@)\D+(.)\D+")
regularny_vyraz = re.compile(r"(\D)*\.\D*.com")
regularny_vyraz = re.compile(r"\d*@\D*.com")
regularny_vyraz = re.compile(r"\S@\D*.com")
regularny_vyraz = re.compile(r"[a-zA-Z]*(\@)\D+(\.)com")

email = input("Zadaj svoj email: ")

vstup_ok = regularny_vyraz.fullmatch(email)
if vstup_ok:
    print("OK")
else:
    print("Nesprávny email")

regularny_vyraz = re.compile(r"[a-zA-Z]?\d?\S{12,30}")
heslo = input("Zadaj heslo: ")

vstup_ok = regularny_vyraz.fullmatch(heslo)
if vstup_ok:
    print("OK")
else:
    print("Nevhodné heslo") 
