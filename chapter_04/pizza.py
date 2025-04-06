pizzas = ['margarita', '4chees', 'cezar', 'el"diablo']
friend_pizzas = pizzas[:]

pizzas.append('martadella')
friend_pizzas.append('with pineapple')

print("My favorite pizzas are:\n")

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("\nMy friend's favorite pizzas are:\n")

for pizza in friend_pizzas:
    print(f"Ilike{pizza} pizza")

print('\n'"I really love pizza!")