#!/bin/python3

#from collections import Counter

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    close = {
        ")": "(", "}": "{", "]": "["
    }
    for i in s:
        if i in ["[", "{", "("] :
            stack.append(i)
        else :
            try :
                if stack.pop() != close[i] :
                    return "NO"
            except :
                return "NO"        
    if stack == [] :
        return "YES" 
    else :
        return "NO" 

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)

