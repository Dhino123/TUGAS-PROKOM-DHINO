def buat_buku(penulis, judul, halaman=None):
    buku = {"penulis": penulis, "judul": judul}
    if halaman:
        buku["halaman"] = halaman
    return buku

while True:
    print("\nMasukkan data buku (ketik 'q' kapan saja untuk berhenti)")

    penulis = input("Nama penulis: ")
    if penulis == "q":
        break

    judul = input("Judul buku: ")
    if judul == "q":
        break

    buku = buat_buku(penulis, judul)
    print(buku)