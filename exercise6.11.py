kota = {
    "Tokyo": {
        "negara": "Jepang",
        "populasi": 14000000,
        "fakta": "Punya penyeberangan jalan Shibuya yang super ramai.",
    },
    "Jakarta": {
        "negara": "Indonesia",
        "populasi": 10600000,
        "fakta": "Dulu namanya Batavia.",
    },
    "Paris": {
        "negara": "Prancis",
        "populasi": 2100000,
        "fakta": "Menara Eiffel selesai dibangun tahun 1889.",
    },
}

for nama_kota, info in kota.items():
    print(f"\n{nama_kota}")
    print(f"Negara: {info['negara']}")
    print(f"Populasi: {info['populasi']}")
    print(f"Fakta: {info['fakta']}")