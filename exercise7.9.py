sandwich_orders = ['tuna', 'pastrami', 'ayam', 'pastrami', 'telur', 'keju', 'pastrami']
finished_sandwiches = []

print("Maaf, pastrami sudah habis.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")