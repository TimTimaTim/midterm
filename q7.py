import random

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(1, 100))

# look at the list using the index
for i in range(len(random_numbers)):

    # if number is odd replace it with its negative value
    if random_numbers[i] % 2 != 0:
        random_numbers[i] = -random_numbers[i]

    else:
        # if even replace it with double value
        random_numbers[i] = random_numbers[i] * 2

# prints final list
print(random_numbers)