def remove_dups(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return res

arr = [1,2,3,4,56,7,8,5,4,3,2,3,47]
print(remove_dups(arr))