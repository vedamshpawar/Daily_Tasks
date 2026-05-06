def repeating_ele(arr):
    res = []
    for i in arr:
        if arr.count(i) > 1:
            res.append(i)
    return set(res)

arr = [1,2,3,4,5,6,5,4,3,2]
print(repeating_ele(arr))