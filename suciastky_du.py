

#Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
#Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. 
#Následně součástku odeber ze slovníku, protože je vyprodaná.
#Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na 
#skladě o množství požadované zákazníkem.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadajte kód produktu: ")
pocet = int(input("Zadajte požadované množstvo: "))

if kod not in sklad:
    print(f"{kod} na sklade nemáme.")

elif sklad [kod] < pocet: 
    print(f" Materiálu {kod} nemáme na sklade dostatok. Môžeme predať len {sklad [kod]} ks. ")
    sklad.pop(kod)
    print(f"Zostávajúci materiál na sklade: {sklad}")

else: 
    print(f" Materiálu {kod} máme na sklade dostatok.")
    novy_stav = sklad[kod] - pocet
    print(f"Zostatok na sklade pre materiál {kod } je {novy_stav} ks. ")




  








    