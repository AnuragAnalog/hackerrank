
def count_substring(string, sub_string):
    tot = 0
    l = len(sub_string)
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i+l] == sub_string:
                tot = tot + 1
    return tot

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
