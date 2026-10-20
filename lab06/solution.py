def count_items(values):
    result = {}
    for key in values:
        if not key in result:
            result[key] = 1
        else:
            result[key] += 1
    return result

def unique_sorted(values):
    return sorted(set(values))

def common(a,b):
    output = []
    for x in a:
        if x in b:
            output.append(x)

    return sorted(output)

def only_in_first(a,b):
    output = []
    for x in a:
        if not x in b:
            output.append(x)

    return sorted(output)

#print(unique_sorted([1,7,3,4,5,8,8]))
print(only_in_first([1, 2 ,7 , 8], [5 ,7 ,8 ,9]))
