# variabel 1
topping = ""
while topping != "quit":
    topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")
    if topping != "quit":
        print(f"Oke, {topping} akan kami tambahkan ke pizza Anda.")