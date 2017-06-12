def get_stats(list):
    result = {'even': 0, 'odd': 0}
    keys = ['even', 'odd']
    for index in range(0, len(list)):
        key = keys[list[index] % 2]
        result[key] += 1
    return result


numbers = [4, 2, 7, 5, 9, 6, 8]
print(get_stats(numbers))
