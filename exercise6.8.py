kucing = {"jenis": "kucing", "pemilik": "dinooo"}
anjing = {"jenis": "anjing", "pemilik": "yanto"}
kelinci = {"jenis": "kelinci", "pemilik": "yanti"}

hewan_peliharaan = [kucing, anjing, kelinci]

for hewan in hewan_peliharaan:
    print(f"Jenis: {hewan['jenis']}")
    print(f"Pemilik: {hewan['pemilik']}\n")