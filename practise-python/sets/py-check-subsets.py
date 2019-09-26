
t = int(input())

for i in range(t):
    la = int(input())
    a = set(map(int, input().split()))
    lb = int(input())
    b = set(map(int, input().split()))
    if la > lb:
        print("False")
    else:
        c = True
        for ele in a:
            if ele in b:
                continue
            else:
                print("False")
                c = False
                break
        if c:
            print("True")
