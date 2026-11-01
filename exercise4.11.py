pizza = ["pepperoni", "keju", "sosis"]
pizza_teman = pizza[:]

pizza.append("jamur")
pizza_teman.append("nanas")

print("Pizza favorit saya:")
for nama in pizza:
    print(nama)

print("Pizza favorit teman saya:")
for nama in pizza_teman:
    print(nama)