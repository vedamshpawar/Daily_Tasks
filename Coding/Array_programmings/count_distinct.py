def count_distinct_ele(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    return len(res)


arr = [12,34,34,56,65,45,32,47,45,56]
print(count_distinct_ele(arr))
