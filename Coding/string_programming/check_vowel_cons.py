def check_vowel_cons(ch):
    vowels = 'aeiouAEIOU'
    if ch in vowels:
        return f'{ch} is vowel'
    else:
        return f'{ch} is consonant'
    
ch = input('enter a number: ')
print(check_vowel_cons(ch))