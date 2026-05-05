def sum_of_n_naturals(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return f'{sum} is sum of natural numbers'

num = int(input('enter a number: '))
print(sum_of_n_naturals(num))