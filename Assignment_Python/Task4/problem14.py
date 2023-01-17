l = range(0,40)
res = list(filter(lambda i : i % 3 != 0 and i % 7 == 0, l))
print(res)