try:
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    result = x / y
    print(f'The result of {x}/{y} is {result}')
except ValueError:
    print('Please enter a valid number')
except ZeroDivisionError:
    print('Cannot divide by zero')

