class MyClass:
    def add(self, x, y, z=None):
        if z:
            return x + y + z
        else:
            return x + y

obj = MyClass()
print(obj.add(1, 2)) # This will output 3
print(obj.add(1, 2, 3)) # This will output 6
