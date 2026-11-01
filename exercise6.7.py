orang_1 = {
    "nama_depan": "Budi",
    "nama_belakang": "Santoso",
    "umur": 20,
    "kota": "Bandung",
}
orang_2 = {
    "nama_depan": "Sari",
    "nama_belakang": "Wulandari",
    "umur": 19,
    "kota": "Semarang",
}
orang_3 = {
    "nama_depan": "Andi",
    "nama_belakang": "Pratama",
    "umur": 21,
    "kota": "Medan",
}

orang_orang = [orang_1, orang_2, orang_3]

for orang in orang_orang:
    print(f"Nama: {orang['nama_depan']} {orang['nama_belakang']}")
    print(f"Umur: {orang['umur']}")
    print(f"Kota: {orang['kota']}\n")