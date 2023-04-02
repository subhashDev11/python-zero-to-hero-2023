# Iterators
class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            result = self.i ** 2
            self.i += 1
            return result
        else:
            raise StopIteration

squares = Squares(5)
for square in squares:
    print(square) # Output: 0 1 4 9 16
