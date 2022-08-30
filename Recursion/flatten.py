def flatten(arr):
    result = []
    for x in arr:
        if type(x) is list:
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

print(flatten([1, 2, 3, [4, 5]]))