def func1(l):
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)
    return nl       
print(func1([1, 1, 2, 2]))
