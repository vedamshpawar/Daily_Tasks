def sorting_elements(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def second_smallest_ele(arr):
    smallest =  sorting_elements(arr)[-2]
    return smallest


arr = [12,34,56,65,45,32,47]
print(second_smallest_ele(arr))