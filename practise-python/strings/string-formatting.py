
def print_formatted(number):
    num = number
    l1 = len(str(num))
    l2 = len(oct(num)[2:])
    l3 = len(hex(num)[2:])
    l4 = len(bin(num)[2:])
    l = max(l1, l2, l3, l4)
    for number in range(1, num+1):
        print(str(number).rjust(l, " ")+" "+oct(number)[2:].rjust(l, " ")+" "+hex(number).upper()[2:].rjust(l, " ")+" "+bin(number)[2:].rjust(l, " "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
