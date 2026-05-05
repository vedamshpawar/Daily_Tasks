def greatest_of_three(num1, num2, num3):
    if num1 > num2:
        return f'{num1} is greater'
    elif num2 > num3:
        return f'{num2} is greater'
    else:
        return f'{num3} is greater'

num1 = int(input('enter a num1: '))
num2 = int(input('enter a num2: '))
num3 = int(input('enter a num3: '))
print(greatest_of_three(num1, num2, num3))