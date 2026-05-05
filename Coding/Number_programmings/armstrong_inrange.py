def armstrong_number(num):
    s_num = str(num)
    total = sum(int(i)**len(s_num) for i in s_num)
    return num == total

def armstrong_inrange(num):
    res = []
    for i in range(11, num + 1):
        if armstrong_number(i):
            res.append(i)
    return res

num = int(input('enter a number: '))
print(armstrong_inrange(num))