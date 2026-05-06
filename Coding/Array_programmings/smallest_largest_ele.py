def smallest_largest_ele(arr):
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]
    return f'{max} is max element, {min} is min element'

arr = [12,34,56,65,45,32,47]
print(smallest_largest_ele(arr))