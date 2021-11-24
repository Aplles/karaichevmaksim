import string


def is_palindrome(stroka):
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

stroka = str(input())
print(is_palindrome(stroka))
