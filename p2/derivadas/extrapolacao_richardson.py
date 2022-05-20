import math

def richardson(col1):
   col1 = [item for item in col1]
   n = len(col1)
   for j in range(n - 1):
      tmp_coluna = [0] * (n - 1 - j)
      for i in range(n - 1 - j):
         power = j + 1 # é igual ao num da coluna anterior
         tmp_coluna[i] = (2 ** power * col1[i + 1] - col1[i]) / (2 ** power - 1)
      col1[:n - 1 - j] = tmp_coluna
      print(tmp_coluna)
   return col1[0] #a aprox. procurada

# def F1(f, x0, h):
#    return (f(x0 + h) - f(x0)) / h

# def F2(f, x0, h):
#    return (f(x0) - f(x0 - h)) / h

# def f(x):
#    return x ** x

# def g(x):
#    return math.cos(2**x)askfjaslkfjasf

#--------------------------------------------------------------------------
#EX 42
# def f(x):
#    return math.cos(x+math.sqrt(math.log(x**2)))

# col1 = [-1.037324908502003, -1.0572214348439315, -1.0622294181123944, -1.063483536242381]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 43
# def f(x):
#    return math.sin(math.cos(math.e**(-x)))

# col1 = [1.3725545403717474, 1.2948036941039973, 1.2850907000147747, 1.284007992326004]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 44
# def f(x):
#    return math.sqrt(math.cos(x**2) + x)

# col1 = [0.5193594141108915, 0.5638945194530582, 0.5666206788892874, 0.5667885388792726]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 45
# def f(x):
   # return math.sin(x)**3 - 3*math.sin(x)**2 \
      # + math.sin(x**2) + 4

# col1 = [-4.400000048386502, -5.034135596461297, -5.194354181732308, -5.234484958808707, -5.24452193788602, -5.247031442988373]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 46
# def f(x):
#    return math.cos(x)**3 + 2*math.cos(x)**2 + 1

# col1 = [4.661073218242419, 4.701200840525241, 4.7039260990591245, 4.704100029478347, 4.704110957270075]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 47
# def f(x):
#    return math.e**(-x**2) + math.cos(x) + 3

# col1 = [0.34703950842598275, 0.39815423156778706, 0.41176928558684267, 0.41521932799878414]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 48
# def f(x):
#    return math.e**(-x**2) + math.cos(x) + 3

# col1 = [-0.10165026941228916, 0.006830715969954326, 0.03248453664127737, 0.03880638559348881, 0.04038190469145775]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 49
# def f(x):
#    return math.sin(x)**4 - 4*math.sin(x)**2 \
#       +math.cos(x**2) + math.e**(-x**2) + 5

# col1 = [-2235.3806897425266, -1477.8784380126174, -1257.4841279653483, -1230.847782750614, -1227.7420999407768]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P2.5
def f(x):
   return math.e**-(x**2) + math.cos(x) + 3

x0 = 4.10614
col1 = [-0.7970192758533159, -0.8155536462971895, -0.8202458689822834, -0.8214225528263341]
#--------------------------------------------------------------------------


if __name__ == "__main__":
   pass
   #x0 = 2
   #h = 0.5
   # col1 = [f'f1({h/2**i})={F1(f, x0, h/2 **i)}' for i in range(6)]
   #col1 = [F1(f, x0, h/2 ** i) for i in range(6)]
   richardson(col1)
