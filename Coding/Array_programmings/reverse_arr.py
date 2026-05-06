def reverse_arr(arr):
    rev = []
    for i in arr:
        rev = [i] + rev
    return rev

arr = [12,34,56,65,45,32,47]
print(reverse_arr(arr))