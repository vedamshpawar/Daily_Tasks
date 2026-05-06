def first_second_half_asc_desc(arr):
    mid = len(arr)//2
    arr.sort()
    first = arr[:mid]
    second = arr[mid:][::-1]
    total = first + second
    return total

arr = [12,34,56,65,45,32,47]
print(first_second_half_asc_desc(arr))
