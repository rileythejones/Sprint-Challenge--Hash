def has_negatives(a):

    cache = {}
    for x in a:
        for y in a:
            look = x + y
            if look == 0:
                if x > 0:
                    cache[x] = y
                    result = list(cache)
                
    return result 


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
