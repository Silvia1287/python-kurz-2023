#\d{1,2}\. ?\d{1,2}\. ?\d{4}
#\d{1,2}\/ ?\d{1,2}\/ ?\d{4}

#Vyhľadávanie pošta: 

#\d{3} ?\d{2}(.*[^0-9])


#Overenie užívateľského mena: 
import re
regularne_meno = re.compile(r"[a-zA-z]{6,10}")

meno= input("Zadajte prihlasovacie meno: ")

meno_ok = regularne_meno.fullmatch(meno)

print(meno_ok)

#Overenie hesla: 
regulerne_heslo =  re.compile (r"\S{12,30}")
heslo = input("Zadajte heslo: ")
heslo_ok = regulerne_heslo.fullmatch(heslo)
print(heslo_ok)

#Overenie emailu: 
#^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}