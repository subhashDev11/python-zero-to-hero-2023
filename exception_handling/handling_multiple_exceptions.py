try:
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    result = x / y
    print(f'The result of {x}/{y} is {result}')
except (ValueError, ZeroDivisionError) as e:
    print(f'An error occurred: {e}')
