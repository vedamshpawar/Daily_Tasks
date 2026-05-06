def largest_element(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [12,34,56,65,45,32,47]
print(largest_element(arr))