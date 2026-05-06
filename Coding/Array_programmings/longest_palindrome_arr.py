def ispalindrome(s):
    return s == s[::-1]

def longest_palindrome_arr(arr):
    longest = ''
    for i in range(len(arr)):
        if ispalindrome(str(arr[i])) and len(str(arr[i])) > len(longest):
            longest = str(arr[i])
    return longest

arr = [121, 234, 4534, 56667, 8778]
print(longest_palindrome_arr(arr))
