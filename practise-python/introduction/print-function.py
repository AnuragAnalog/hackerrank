
if __name__ == '__main__':
    n = int(input())

    tot = "1"
    for i in range(n-1):
        tot = tot + str(i+2)
    print(tot)
