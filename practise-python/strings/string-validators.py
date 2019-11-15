
if __name__ == '__main__':
    s = input()

    f = 0
    for c in s:
        if c.isalnum():
            print(True)
            f = 1
            break
    if f == 0:
        print(False)
    f = 0
    for c in s:
        if c.isalpha():
            print(True)
            f = 1
            break
    if f == 0:
        print(False)
    f = 0
    for c in s:
        if c.isdigit():
            print(True)
            f = 1
            break
    if f == 0:
        print(False)
    f = 0
    for c in s:
        if c.islower():
            print(True)
            f = 1
            break
    if f == 0:
        print(False)
    f = 0
    for c in s:
        if c.isupper():
            print(True)
            f = 1
            break
    if f == 0:
        print(False)
