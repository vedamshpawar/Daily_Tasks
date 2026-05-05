def Positive_negative_nums(num):
    if num > 0:
        return f'Positive number'
    else:
        return f'Negative'

num = int(input('enter a number: '))
print(Positive_negative_nums(num))