
def split_and_join(line):
    tmpstr = line.split()
    return "-".join(tmpstr)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
