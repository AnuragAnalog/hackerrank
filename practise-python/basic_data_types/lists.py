
if __name__ == '__main__':
    l = list()
    N = int(input())

    for i in range(N):
        task = input().split()
        if task[0] == "insert":
            l.insert(int(task[1]), int(task[2]))
        elif task[0] == "print":
            print(l)
        elif task[0] == "remove":
            l.remove(int(task[1]))
        elif task[0] == "append":
            l.append(int(task[1]))
        elif task[0] == "pop":
            l.pop()
        elif task[0] == "sort":
            l.sort()
        elif task[0] == "reverse":
            l.reverse()
