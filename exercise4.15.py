# exercise4.1
pizza = ["pepperoni", "keju", "sosis"]

for nama in pizza:
    print(f"Saya suka pizza {nama}.")

print("piza enak pol!")

# exercise4.8
kubus = []
for n in range(1, 11):
    kubus.append(n ** 3)

for k in kubus:
    print(k)

# exercose4.13
# poin A
menu = ("nasi", "ayam goreng", "tempe", "sayur asem", "telur")

for makanan in menu:
    print(makanan)

# poin B
# menu[0] = "mie"  (sebelumnya tidak saya kasih pagar karena saya ingin menampilkan errornya, tapi sekarang saya kasih pagar agar tidak error)

# poin C
menu = ("nasi", "ayam goreng", "tempe", "sayur asem", "telur")

for makanan in menu:
    print(makanan)

# menu[0] = "mie"  

menu = ("nasi", "ikan bakar", "tempe", "sayur asem", "tahu")

print("Menu baru:")
for makanan in menu:
    print(makanan)