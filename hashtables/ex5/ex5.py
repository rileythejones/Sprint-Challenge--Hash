import re 


def finder(files, queries):

    cache = {}
    for x in files:
        cache[x] = re.findall("([^\/]+$)", x)[0]

    results = []
    for x in cache:
        if cache[x] in queries:
            results.append(x)
    
    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
