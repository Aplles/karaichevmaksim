def count_words(string):
    signs = ['.', ',', ';', ':', '!', '?', '&', '-', '"', '\'', '(', ')']
    for i in string:
        for j in signs:
            string = string.replace(j, '')
    lst = string.lower().split()
    dict = {}
    for word in lst:
        if type(word) == str and word not in dict:
            dict[word] = 1
        elif type(word) == str:
            dict[word] += 1
    return dict


print(count_words("A man, a plan, a canal -- Panama"))
# => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo"))
# => {"doo": 3, "bee": 2}
