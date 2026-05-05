def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def strong_number(num):
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum += factorial(digit)
        num //= 10
    return sum == temp

num = int(input('enter a number: '))
print(strong_number(num))
