import math

def richardson(col1):
    col1 = [item for item in col1] # copia da coluna 1
    n = len(col1)
    for j in range(n-1):
        temp_col = [0] * (n - 1 - j)
        for i in range (n - 1 - j):
            power = j + 1 # é igual o numero da coluna anterior
            temp_col[i] = (2 ** power * col1[i + 1] - col1[i] / (2 ** power - 1))
        col1[:n - 1 - j] = temp_col
        print(temp_col)
    return col1[0]

def F1(f, x0, h):
    return (f(x0 + h) - f(x0)) / h

def F2(f, x0, h):
    return (f(x0) - f(x0 - h)) / h

def f(x):
    return x ** x

h = 0.44049
x0 = -0.15452
col1 = [F2(f, x0, h / 2 ** i) for i in range(4)]

r = richardson(col1)
print(r)

# F20 = (2**19 * F19(h/2) - F19(h)) / (2**19 -1)
# (2**1 * F1(h/2**20) - F1(h/2**19)) / (2*1 - 1)

def g(x):
    return math.cos(2 **x)