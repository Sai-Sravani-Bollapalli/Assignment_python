def s(a,b):
    l1 = len(a)
    l2 = len(b)
    if l1 > l2:
        print(a)
    elif l1 <l2:
        print(b)
    elif l1 == l2:
        print(a,"\n",b)
s("hello", "world")