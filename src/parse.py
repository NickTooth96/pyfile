def string_distance(str_0, str_1):
    min_len = min(len(str_0), len(str_1))
    len_diff = abs(len(str_0) - len(str_1))
    if len(str_0) == 0:
        return len(str_1)
    if len(str_1) == 0:
        return len(str_0)
    string_distance = 0
    for i in range(min_len):
        if str_0[i] != str_1[i]:
            string_distance += 1
    return string_distance + len_diff
        
print(string_distance("hello", "world"))
