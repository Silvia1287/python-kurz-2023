class Auto:
    def __init__(self, registracna_znacka, typ_vozidla, najazdene_km):
        self.registracna_znacka = registracna_znacka
        self.typ_vozidla = typ_vozidla
        self.najazdene_km = najazdene_km
        self.dostupne = True
 
        
    def pozicaj_auto (self):
        if self.dostupne == True:
            self.dostupne =  False
            return f" Potvrdzujeme prenájom auta."
        else: 
            return f" Vozidlo nie je dostupné. "
            
    def get_info(self):
        return f"Zvolené auto {self.typ_vozidla} ma registračnú značku {self.registracna_znacka}."
            
    
peugeot = Auto("4A2 3020","Peugeot 403 Cabrio", "47534")
skoda = Auto("1P3 4747", "Škoda Octavia", "41253") 

pozicat = input("Aké auto si chcete požičať? ")
if pozicat == "skoda":
   print (skoda.pozicaj_auto())
   print (skoda.get_info())

else:
    print(peugeot.pozicaj_auto())
    print(peugeot.get_info())

pozicat = input("Aké auto si chcete požičať? ")
if pozicat == "skoda":
   print (skoda.pozicaj_auto())
  
else:
    print(peugeot.pozicaj_auto())