l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(filter(lambda i : i % 2 == 0, l))
res = list(map(lambda j: j * j, l1))
print("Squares of even in given list:", res)