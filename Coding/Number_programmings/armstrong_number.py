def armstrong_number(num):
    s_num = str(num)
    total = sum(int(i)**len(s_num) for i in s_num)
    return num == total

num = int(input('enter a number: '))
print(armstrong_number(num))