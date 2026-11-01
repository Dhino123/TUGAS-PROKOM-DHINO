bahasa_favorit = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

orang_orang = ["jen", "dhino", "phil", "budi", "sarah"]

for nama in orang_orang:
    if nama in bahasa_favorit:
        print(f"Makasih {nama}, udah ikut polling!")
    else:
        print(f"Hai {nama}, ikut polling bahasa favorit yuk!")