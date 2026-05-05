def reverse_of_num(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev*10 + digit
        num //= 10
    return rev

def ispalindrome(num):
    return num == reverse_of_num(num)

num = int(input('enter a number: '))
print(ispalindrome(num))