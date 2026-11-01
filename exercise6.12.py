kota = {
    "Tokyo": {
        "negara": "Jepang",
        "benua": "Asia",
        "populasi": 14000000,
        "fakta": "Punya penyeberangan jalan Shibuya yang super ramai.",
    },
    "Jakarta": {
        "negara": "Indonesia",
        "benua": "Asia",
        "populasi": 10600000,
        "fakta": "Dulu namanya Batavia.",
    },
    "Paris": {
        "negara": "Prancis",
        "benua": "Eropa",
        "populasi": 2100000,
        "fakta": "Menara Eiffel selesai dibangun tahun 1889.",
    },
}

print("=== KARTU INFO KOTA ===")

for nama_kota, info in kota.items():
    print("\n" + "-" * 30)
    print(nama_kota.upper())
    print("-" * 30)
    print(f"Negara   : {info['negara']} ({info['benua']})")
    print(f"Populasi : sekitar {info['populasi']} orang")
    print(f"Fakta    : {info['fakta']}")