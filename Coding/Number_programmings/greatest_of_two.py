def greatest_of_two(num1, num2):
    if num1 > num2:
        return f'{num1} is greater'
    else:
        return f'{num2} is greater'

num1 = int(input('enter a num1: '))
num2 = int(input('enter a num2: '))
print(greatest_of_two(num1, num2))