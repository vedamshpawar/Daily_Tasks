def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_inrange(num):
    primes = []
    for i in range(num + 1):
        if prime(i):
            primes.append(i)
    return primes

num = int(input('enter a number: '))
print(prime_inrange(num))