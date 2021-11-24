def combine_anagrams(words_array):
    dict = {}
    for word in words_array:
        if ''.join(sorted(word)) not in dict:
            dict[''.join(sorted(word))] = [word]
        else:
            dict[''.join(sorted(word))] += [word]
    lst = []
    for values in dict.values():
        lst.append(values)
    return lst


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
# => [["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"]]
