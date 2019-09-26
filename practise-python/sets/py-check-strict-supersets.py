
A = set(map(int, input().split()))
n = int(input())

def strict_superset(A, sets):
    if len(A) <= len(sets):
        return False
    else:
        for ele in sets:
            if ele not in A:
                return False
        return True

for i in range(n):
    c = True
    sets = set(map(int, input().split()))

    if not strict_superset(A, sets):
        print("False")
        c = False
        break
if c:
    print("True")
