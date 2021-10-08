#!/bin/python3

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result = []
    for i in queries :
        result.append(strings.count(i))
    return result

if __name__ == '__main__':

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))