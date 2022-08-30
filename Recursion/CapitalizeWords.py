def capitalize(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].title())
    return result+ capitalize(arr[1:])

print(capitalize(['I', 'Am', 'Learning']))