def gen():
    yield 1
    yield 2
    yield 9

for value in gen():
    print(value)