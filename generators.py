numbers = [1, 2, 3]

it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

print("next example")


word = "cat"
it_word = iter(word)

for letter in it_word:
    print(letter)

print("next example")


class SimpleCounter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

print("next example")

def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)

print("next example")


def count_down(n):
    while n > 0:
        yield n
        n -= 1

for number in count_down(3):
    print(number)

print("next example")

squares = (x * x for x in range(1, 4))

for s in squares:
    print(s)
