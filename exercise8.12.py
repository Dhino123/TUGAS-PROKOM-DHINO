def pesan_pizza(*topping):
    print("\nPesanan pizza dengan topping:")
    for item in topping:
        print(f"- {item}")

pesan_pizza("keju")
pesan_pizza("sosis", "jamur")
pesan_pizza("keju", "sosis", "paprika", "nanas")