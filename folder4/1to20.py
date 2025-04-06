numbers = [i for i in range(1,1000_000)]
print(numbers)

for i in range(1,21):
    print(i)

numbers = []
for i in range(1,1_000_000):
    numbers.append(i)
print(numbers)

print(min(numbers), max(numbers), sum(numbers))

numbers = [number for number in range(1,21,2)]
print(numbers)

numbers = list(range(3,30,3))
for number in numbers:
    print(number)

numbers = list(range(1,11))
for number in numbers:
    print(number**3)

numbers = [number**3 for number in range(1,11)]
print(numbers)