# Complete the solve function below.
def solve(s):
    i=s.replace(s[0],s[0].upper())
    stri=""
    count = 0
    for x in i:
        if s[count-1]==' ':
            stri+=i[count].upper()
        else:
            stri+=i[count]
        count+=1
    return stri
