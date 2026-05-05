def factor_of_number(num):
    res = []
    for i in range(1, num+1):
        if num % i == 0:
            res.append(i)

    return res

num = int(input('enter a number: '))
print(factor_of_number(num))