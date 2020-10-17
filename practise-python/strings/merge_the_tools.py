def merge_the_tools(string, k):
    chunks = len(string)//k
    for idx in range(chunks):
        t = string[idx * k : (idx+ 1) * k]
        u = ""
        for c in t:
            if c not in u:
                u += c
        print(u)
