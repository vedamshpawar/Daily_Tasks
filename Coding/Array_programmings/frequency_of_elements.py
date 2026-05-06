def frequency_of_elements(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

arr = [12,34,56,65,45,32,47,34,45,56,12,34,65]
print(frequency_of_elements(arr))
