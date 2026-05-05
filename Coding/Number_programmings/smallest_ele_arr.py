def smallest_element(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

arr = [12,34,56,65,45,32,47]
print(smallest_element(arr))