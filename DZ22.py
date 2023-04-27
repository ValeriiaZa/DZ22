def find_unique_value(some_list):
    a = 0
    for el in some_list:
        if some_list.count(el) >= 2:
            continue
        else:
            break
    return el
lst = [5, 5, 5, 2, 2, 0.5]
print(find_unique_value(lst))

