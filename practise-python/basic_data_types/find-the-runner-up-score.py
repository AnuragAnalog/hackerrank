
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = set(arr)
    arr.remove(max(arr))
    print(max(arr))
