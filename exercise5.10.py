pengguna_sekarang = ["asep", "dhino", "naja", "netanyahu", "prabowo"]
pengguna_baru = ["naja", "marin", "futaba", "sawako", "waguri"]

pengguna_kecil = []
for nama in pengguna_sekarang:
    pengguna_kecil.append(nama.lower())

for nama in pengguna_baru:
    if nama.lower() in pengguna_kecil:
        print(f"{nama} AKU SAYANG KAMU")
    else:
        print(f"{nama} AKU JUGA SAYANG SAMA KAMU")