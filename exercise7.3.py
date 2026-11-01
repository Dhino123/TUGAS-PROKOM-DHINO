angka = input("Masukkan sebuah angka: ")
angka = int(angka)

if angka % 10 == 0:
    print(f"{angka} adalah kelipatan 10.")
else:
    print(f"{angka} bukan kelipatan 10.")