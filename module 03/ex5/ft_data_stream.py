
def count():
    yield 1
    yield 2
    yield 3

# print(next(count()))
# print(next(count()))


i = count()
print(next(i))
print(next(i))
# print(next(i))
# print(next(i))