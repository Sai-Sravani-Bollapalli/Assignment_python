from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7]
res = int(reduce(lambda a, b: 10 * a + b, l))
print(res)