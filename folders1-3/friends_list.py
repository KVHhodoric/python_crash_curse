wish_list = ['Kate', 'Bobre', 'Kurwe', 'Annet']
message = 'We are wait you in the house'

print(wish_list[2])
del wish_list[2]
wish_list.append('Kolya')

print(f"{message} {wish_list[0].title()}")
print(f"{message} {wish_list[1].title()}")
print(f"{message} {wish_list[-1].title()}")
print(f"{message} {wish_list[-2].title()}")

print('We have more guest')

wish_list.insert(0, 'Nastya')
wish_list.insert(3, 'Nikita')
wish_list.append('Nina')

print(f"{message} {wish_list[0].title()}")
print(f"{message} {wish_list[1].title()}")
print(f"{message} {wish_list[2].title()}")
print(f"{message} {wish_list[3].title()}")
print(f"{message} {wish_list[-3].title()}")
print(f"{message} {wish_list[-2].title()}")
print(f"{message} {wish_list[-1].title()}")
print(len(wish_list))
print("I have a probleme , with my dinner table, i have only 2 sits")
message_2 =("Oh I'm sorry but new dinner table cannot receive at time, i decline you'r priglasitelnii")

print(f"{message_2} {wish_list.pop(-1)}")
print(f"{message_2} {wish_list.pop(-1)}")
print(f"{message_2} {wish_list.pop(-1)}")
print(f"{message_2} {wish_list.pop(-1)}")
print(f"{message_2} {wish_list.pop(-1)}")

print(f"{message} {wish_list[0]}")
print(f"{message} {wish_list[1]}")

del wish_list[0]
del wish_list[0]
print(wish_list)