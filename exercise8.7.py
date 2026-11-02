def buat_buku(penulis, judul, halaman=None):
    buku = {"penulis": penulis, "judul": judul}
    if halaman:
        buku["halaman"] = halaman
    return buku

buku1 = buat_buku("Andrea Hirata", "Laskar Pelangi")
buku2 = buat_buku("Tere Liye", "Bumi")
buku3 = buat_buku("Dee Lestari", "Supernova", halaman=250)

print(buku1)
print(buku2)
print(buku3)