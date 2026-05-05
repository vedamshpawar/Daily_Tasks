def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_factors(num):
    res = []
    for i in range(1, num + 1):
        if num % i == 0 and isprime(i):
            res.append(i)
    return res

num = int(input('enter a number: '))
print(prime_factors(num))