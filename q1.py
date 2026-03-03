def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

numbers = [
    "5485839837501070045005400701057389385845",
    "8025833559061079503003059701609553385208",
    "748961771974924464636564429479177169847",
    "6593036601359343374664733439531066303956"
]

for n in numbers:
    print(n, "->", palindrome(n))