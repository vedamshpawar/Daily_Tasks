def non_repeating_ele(arr):
    res = []
    for i in arr:
        if arr.count(i) == 1:
            res.append(i)
    return res

arr = [1,2,3,4,56,7,8,5,4,3,2,3,47]
print(non_repeating_ele(arr))