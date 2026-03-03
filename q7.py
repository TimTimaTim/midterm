import random

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Go through the list using index because we want to modify values
for i in range(len(random_numbers)):

    # If number is odd
    if random_numbers[i] % 2 != 0:
        # Replace it with its negative value
        random_numbers[i] = -random_numbers[i]

    else:
        # If number is even, replace it with double value
        random_numbers[i] = random_numbers[i] * 2

# Print final list
print(random_numbers)