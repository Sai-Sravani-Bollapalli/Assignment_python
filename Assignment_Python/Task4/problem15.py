l = [1, 2, 3, 4, 5]
def tfun(i):
        return i * i      
res = list(map(tfun,l))
print("Multiply list by itself:", res)