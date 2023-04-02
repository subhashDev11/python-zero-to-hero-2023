try:
    age = int(input('Enter your age: '))
    if age < 0:
        raise ValueError('Age cannot be negative')
    print(f'Your age is {age}')
except ValueError as e:
    print(f'An error occurred: {e}')
