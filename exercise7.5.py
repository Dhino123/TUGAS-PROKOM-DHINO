while True:
    umur = int(input("Berapa umur Anda? "))

    if umur < 3:
        print("Tiket Anda gratis.")
    elif umur <= 12:
        print("Harga tiket Anda $10.")
    else:
        print("Harga tiket Anda $15.")