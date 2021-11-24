def max_odd(array):
    result = []
    for i in array:
        if type(i) == int or type(i) == float:
            if i % 2 == 1:
                result.append(i)
    if len(result) != 0:
        max_ne_chet = max(result)
        return int(max_ne_chet)
    else:
        return None

print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))