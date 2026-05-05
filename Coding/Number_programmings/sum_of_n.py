def sum_of_n(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return f'{sum} is sum of n-nums'

num = int(input('enter a numbers: '))
print(sum_of_n(num))