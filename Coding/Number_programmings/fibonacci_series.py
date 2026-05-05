def fibo_series(num):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, num + 1):
        temp = a + b
        a = b
        b = temp
        print(temp)
    
num = int(input('enter a number: '))
fibo_series(num)