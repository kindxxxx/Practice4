numbers = [1, 2, 3]

it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

word = "cat"
it_word = iter(word)

for letter in it_word:
    print(letter)
