import string


def is_palindrome(stroka):
    stroka = str(stroka)
    stroka = stroka.replace(' ', '').lower()
    stroka = ''.join(i for i in stroka if i.isalpha())
    is_pal = True
    lens = len(stroka)
    for i in range(len(stroka) // 2):
        if stroka[i] == stroka[lens - 1]:
            lens -= 1
        else:
            is_pal = False
            break
    return is_pal

print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False
