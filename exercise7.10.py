responses = {}

polling_active = True

while polling_active:
    name = input("\nSiapa nama Anda? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Apakah ada orang lain yang mau menjawab? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Hasil Polling ---")
for name, place in responses.items():
    print(f"{name} ingin pergi ke {place}.")