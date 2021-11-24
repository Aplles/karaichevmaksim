def connect_dicts(dict1, dict2):
    dict = {}
    sum_dict1 = 0
    for values in dict1.values():
        sum_dict1 += values
    sum_dict2 = 0
    for values in dict2.values():
        sum_dict2 += values
    if sum_dict1 < sum_dict2:
        dict1.update(dict2)
        dict = dict1.copy()
    elif sum_dict1 > sum_dict2:
        dict2.update(dict1)
        dict = dict2.copy()
    elif sum_dict2 == sum_dict1:
        dict1.update(dict2)
        dict = dict1.copy()
    del_key = []
    for key, values in dict.items():
        if values < 10:
            del_key.append(key)
    for i in del_key:
        del dict[i]
    sort_keys = sorted(dict, key=dict.get)
    sorted_dict = {}
    for i in sort_keys:
        sorted_dict[i] = dict[i]
    return sorted_dict


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
# => { "c": 11, "b": 12 }
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
# => { d: 11, "c": 12, "a": 13 }
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
# => { "c": 11, "b": 12, "a": 15 }
