kota = ["Solo", "Bandung", "Surabaya", "Semarang", "Yogyakarta"]

kota.append("Medan")
kota.insert(1, "Jakarta")
print(kota)

del kota[0]
print(kota)

terakhir = kota.pop()
print(terakhir)

kota.remove("Bandung")
print(kota)

kota.sort()
print(kota)
print(sorted(kota, reverse=True))

kota.reverse()
print(kota)

print(len(kota))