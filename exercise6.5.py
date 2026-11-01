sungai = {
    "Nil": "Mesir",
    "Amazon": "Brasil",
    "Kapuas": "Indonesia",
}

for nama, negara in sungai.items():
    print(f"Sungai {nama} mengalir di {negara}.")

print("\nNama sungai:")
for nama in sungai.keys():
    print(nama)

print("\nNama negara:")
for negara in sungai.values():
    print(negara)