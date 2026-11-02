def proses_belanjaan(belum_dibeli, sudah_dibeli):
    while belum_dibeli:
        barang = belum_dibeli.pop()
        print(f"Membeli {barang}")
        sudah_dibeli.append(barang)

belanjaan = ["beras", "telur", "minyak goreng"]
terbeli = []

proses_belanjaan(belanjaan[:], terbeli)

print("\nBelanjaan asli:", belanjaan)
print("Sudah dibeli:", terbeli)