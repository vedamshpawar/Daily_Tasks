def Even_Odd(num):
    if num % 2 == 0:
        return f'{num} is Even number'
    if num % 2 == 1:
        return f'{num} is Odd number'
    else:
        return f'Invalid number'

num = int(input('enter a number: '))
print(Even_Odd(num))