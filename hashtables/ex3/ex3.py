def intersection(arrays):

    cache = {}
    for x in arrays:
        for y in x:
            if cache.get(y) == None:
                cache[y] = 0
            cache[y] = cache.get(y) + 1
    
    len(arrays)
    result = [ x for x, y in cache.items() if y==len(arrays)]
    result

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
