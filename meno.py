meno = "Silvia" 
input(meno + "czechitas.cz") 
print(input) 

#veľke písmená
meno_priezvisko = input("Zadaj svoje meno a priezvisko: ")
print(meno_priezvisko.upper())

#malé písmená
meno_priezvisko = input("Zadaj svoje meno a priezvisko: ")
print(meno_priezvisko.lower())


#iniciály
meno = input("Zadaj meno: ")
priezvisko = input("Zadaj priezvisko: ")
inicialy = meno[0] + priezvisko[0]
print("Tvoje iniciály sú:", inicialy.upper())

meno= input ("Zadaj svoje meno: ")
priezvisko = input("Zadaj priezvisko: ")

#podmienka if
meno = input("Zadaj krstné meno: ")
priezvisko = input("Zadaj priezvisko: ")

len(meno)

if len (meno)>5:
    print(meno[0] + "." + priezvisko)
else:
    print(meno + "." + priezvisko)
