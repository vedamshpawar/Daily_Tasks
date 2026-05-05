def factorial_number(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

num = int(input('enter a number: '))
print(factorial_number(num))