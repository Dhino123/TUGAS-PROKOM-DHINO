makanan_saya = ["pizza", "nasi goreng", "bakso"]
makanan_teman = makanan_saya[:]

makanan_saya.append("sate")
makanan_teman.append("es krim")

print("Makanan favorit saya:")
for makanan in makanan_saya:
    print(makanan)

print("Makanan favorit teman saya:")
for makanan in makanan_teman:
    print(makanan)