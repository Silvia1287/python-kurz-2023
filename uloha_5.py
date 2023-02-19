teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#priemer teplôt
for hodnota in teploty:
    priemer = sum(hodnota) / len(hodnota)
    print(f"Priemerná teplota bola: {round(priemer, 2)} stupňov. ")

#ranná teplota
print([f"ranné teploty boli: {teplota[0]} stupňa" for teplota in teploty])

#nočná teplota
print([f"nočné teploty boli: {teplota[3]} stupňa" for teplota in teploty])

#poovedená a nočná teplota
print([f"Poobedná teplota bola: {teplota[1]} a nočná: {teplota[3]} stupňov" for teplota in teploty])
