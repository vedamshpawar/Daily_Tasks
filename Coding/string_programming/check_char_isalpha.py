def check_char_isalpha(char):
    if char.isalpha():
        return True
    else:
        return False
    
char = input('enter a char: ')
print(check_char_isalpha(char))
