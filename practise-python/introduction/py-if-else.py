
N = int(input())

if N%2 == 1:
    print("Weird")
elif N >= 2 and N <= 5 and N%2 == 0:
    print("Not Weird")
elif N >= 6 and N <= 20 and N%2 == 0:
    print("Weird")
elif N > 20 and N%2 == 0:
    print("Not Weird")
