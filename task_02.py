def coincidence(list=[], range_num=[]):
    if len(list) != 0 and len(range_num) != 0:
        result = []
        for i in list:
            if type(i) == int or type(i) == float:
                if min(range_num) <= i <= max(range_num):
                    result.append(i)
        return result
    else:
        return list


print(coincidence([1, 2, 3, 4, 5, 'foo'], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))

