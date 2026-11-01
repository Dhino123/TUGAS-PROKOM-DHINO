tempat_favorit = {
    "dhino": ["Bromo", "Malioboro"],
    "budi": ["Bali"],
    "sari": ["Raja Ampat", "Dieng", "Bandung"],
}

for nama, tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama}:")
    for t in tempat:
        print(f"- {t}")