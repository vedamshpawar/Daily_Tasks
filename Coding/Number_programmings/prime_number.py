def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

num = int(input('enter a number: '))
print(isprime(num))