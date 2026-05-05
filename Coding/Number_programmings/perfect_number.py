def proper_factors(num):
    res = []
    for i in range(1, num):
        if num % i == 0:
            res.append(i)
    return res

def perfect_number(num):
    return num == sum(proper_factors(num))

num = int(input('enter a number: '))
print(perfect_number(num))