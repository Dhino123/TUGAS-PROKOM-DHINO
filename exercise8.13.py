def buat_biodata(depan, belakang, **tambahan):
    biodata = {"depan": depan, "belakang": belakang}
    for kunci, nilai in tambahan.items():
        biodata[kunci] = nilai
    return biodata

profil = buat_biodata("Budi", "Santoso",
                      kota="Solo",
                      hobi="memancing",
                      pekerjaan="guru")
print(profil)