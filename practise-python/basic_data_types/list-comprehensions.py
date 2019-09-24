
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    biglist = list()

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sublist = list()
                sublist.append(i)
                sublist.append(j)
                sublist.append(k)
                if sum(sublist) == n:
                    continue
                biglist.append(sublist)
    print(biglist)
