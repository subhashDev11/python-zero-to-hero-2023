# Generator
def squares(n):
    for i in range(n):
        yield i ** 2

for square in squares(5):
    print(square) # Output: 0 1 4 9 16
