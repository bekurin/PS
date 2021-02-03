def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a

a, b = map(int, input().split())
value = Euclidean(a, b)
print(value)
print(a * b // value)