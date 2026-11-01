prodi = "Teknik Industri UNS"
nama = "dhino"
umur = 19
kelas = ["snbp", "snbt", "mandiri"]

# tes string
print("prodi == 'Teknik Industri UNS'?", prodi == "Teknik Industri UNS")
print("prodi == 'Teknik Informasi'?", prodi == "Teknik Informasi")
print("nama != 'dhini'?", nama != "dhini")
print("nama != 'dhino'?", nama != "dhino")

# tes lower()
print("prodi.lower() == 'teknik industri uns'?",
      prodi.lower() == "teknik industri uns")
print("prodi == 'teknik industri uns'?", prodi == "teknik industri uns")

# tes angka
print("umur == 19?", umur == 19)
print("umur == 20?", umur == 20)
print("umur != 20?", umur != 20)
print("umur != 19?", umur != 19)
print("umur > 17?", umur > 17)
print("umur < 17?", umur < 17)
print("umur >= 19?", umur >= 19)
print("umur >= 20?", umur >= 20)
print("umur <= 19?", umur <= 19)
print("umur <= 18?", umur <= 18)

# tes and / or
print("umur > 17 and umur < 25?", umur > 17 and umur < 25)
print("umur > 19 and umur < 22?", umur > 19 and umur < 22)
print("umur < 17 or umur > 18?", umur < 17 or umur > 18)
print("umur < 17 or umur > 25?", umur < 17 or umur > 25)

# tes in / not in
print("'snbp' in kelas?", "snbp" in kelas)
print("'tka' in kelas?", "tka" in kelas)
print("'tka' not in kelas?", "tka" not in kelas)
print("'snbp' not in kelas?", "snbp" not in kelas)