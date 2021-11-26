def sort_list(lst):
    if len(lst) > 0:
        max_num = max(lst)  # максимальное число
        min_num = min(lst)  # минимальное число
        for i in range(len(lst)):
            if lst[i] == min_num:
                lst[i] = max_num
            elif lst[i] == max_num:
                lst[i] = min_num
        lst.append(min_num)
        return lst
    else:
        return lst

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
