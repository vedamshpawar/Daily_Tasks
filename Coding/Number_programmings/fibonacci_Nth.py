def fibo_Nth_series(num):
    a = 0
    b = 1
    for i in range(2, num + 1):
        temp = a + b
        a = b
        b = temp
    return b

num = int(input('enter a number: '))
print(fibo_Nth_series(num))