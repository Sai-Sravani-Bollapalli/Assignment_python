# Swapping the variables
a = 2
b = 1
print ("Before Swapping: a =", a, " b =", b)
temp = a
a = b
b = temp
print ("After Swapping using third variable: a = ", a, " b =", b)
a = a + b
b = a - b
a = a - b
print ("After Swapping without third variable: a = ", a, " b =", b)
