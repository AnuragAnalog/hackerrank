'''
Encryption is transform some readable to not readable 
by sorting following rules.
Explanation:
    The sentence: 'feed the dog' --> passing join = 'feedthedog'
    Encryption:    
    feed
    thed
    og
        Encription takes letters of wich collum: 'fto ehg ee dd'
'''

from math import sqrt


def encryption(s):
    l = len(s)
    sql = sqrt(l)
    rou = round(sql)

    if sql > rou:
        row, col = rou, (rou+1)
    else:
        row, col = rou, rou

    if len(s) < (row*col):
        auto_increment = row*col-len(s)
        s_increment = s+' '*auto_increment
    else:
        s_increment = s
    s_sliced = [s_increment[(m-1)*col:m*col] for m in list(range(1, row+1))]

    str_encpt = []
    for r in list(range(col)):
        for m in s_sliced:
            if r <= (len(m)-1):
                str_encpt += m[r]

    encrypt = ''.join(str_encpt)

    encrypt_sliced = [encrypt[(nn-1)*row:nn*row]
                      for nn in list(range(1, col+1))]

    encrypt_ss = [ss.strip() for ss in encrypt_sliced]
    encrypt_final = ' '.join(encrypt_ss)
    print(encrypt_final)
    return encrypt_final

    '''Entry with a setence to encryption.
        Some samples: 
            haveaniceday --> hae and via ecy
            feedthedog   --> fto ehg ee dd
            chillout     --> clu hlt io
    '''


if __name__ == "__main__":
    cont = 0
    while cont < 2:
        if cont == 0:
            print('The sentence: "Feed the dog" encrypted: ' +
                  encryption('feedthedog'))
        print('**************************')
        encryption(''.join(input('Put your sentence: ').split()))
        print('==========================')
        cont += 1
