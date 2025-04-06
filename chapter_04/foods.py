my_foods = ['pizza', 'falaafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)


print("The first three items in the list are:", my_foods[:3])
print("the items from the middle of the list area:", friend_foods[1:4])
print("The last three items in the list are:", my_foods[-3:])