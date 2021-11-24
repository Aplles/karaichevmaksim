def multiply_numbers(inputs=''):
    s = str(inputs).lower()
    lst = []
    mn = 1
    for i in range(len(s)):
        if s[i].isdigit():
            lst.append(int(s[i]))
    if len(lst) != 0:
        for i in lst:
            mn *= int(i)
        return mn
    else:
        return None


print(multiply_numbers())  # => None
print(multiply_numbers('ss'))  # => None
print(multiply_numbers('1234'))  # => 24
print(multiply_numbers('sssdd34'))  # => 12
print(multiply_numbers(2.3))  # => 6
print(multiply_numbers([5, 6, 4]))  # => 120
