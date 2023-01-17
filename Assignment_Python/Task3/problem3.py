from functools import reduce
ele = [1, 2, 3, 4, 5]
sum = sum(ele)
print(" Sum of all items in a given list:", sum)
mul = reduce((lambda a, b : a * b), ele)
print(" Multiplication of all items in a given list:", mul)
