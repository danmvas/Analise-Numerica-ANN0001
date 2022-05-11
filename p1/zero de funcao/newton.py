import math

####--####--####--####--####--##
# #Exercise 8
# def f(x):
#    return math.e**(5*x) - 2

# def df(x):
#    return 5*math.e**(5*x)

# x0 = 0.57934
# numIteracao = 10
####--####--####--####--####--##
####--####--####--####--####--##
# #Exercise 9
#def f(x):
#   return math.pi*x - math.e**x

#def df(x):
#   return math.pi - math.e**x

# x0 = 2.19082
# numIteracao = 5
####--####--####--####--####--##
# #Exercise 10

# def f(x):
#   return 2*(x+1)*(x-1/2)*(x-1)

# def df(x):
#   return 6*x**2 - 2*x - 2

# x0 = 0.07678
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 11

# def f(x):
#   return x**3 - 7*x**2 + 14*x - 7

# def df(x):
#   return 3*x**2 -14*x + 14

# x0 = 0.27116
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 12

#def f(x):
#   return math.sqrt(x) - math.cos(x)

#def df(x):
#   return 1/(2*math.sqrt(x)) + math.sin(x)

# x0 = 0.2407
# numIteracao = 5
####--####--####--####--####--##

####--####--####--####--####--##
#Exercise 13

# def f(x):
#   return x**4 - 2*x**3 - 3*x**2 + 3*x + 2

# def df(x):
#   return 4*x**3 - 6*x**2 -6*x +3

# x0 = -1.77411
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 14

# def f(x):
#   return x + 1 - 3*math.sin(x)

# def df(x):
#   return 1 - 3*math.cos(x)

# x0 = -1.56162
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 27

# def f(x):
#   return math.e**(5*x) - 2

# def df(x):
#   return 5*math.e**(5*x)

# x0 = -1.16733114
# numIteracao = 700
####--####--####--####--####--##

###--####--####--####--####--##
# PROVA - 2

#def f(x):
#  return x**2 - 2

#def df(x):
#  return 2*x

###--####--####--####

#def f(x):
#  return x**2 - 4*x + 2 - math.log(x)

#def df(x):
#  return 2*x - 4 - 1/x

# x0=-1.16779128
# numIteracao = 700

###--####--####--####--####--##

# QUESTÃO ESCROTA DA ÁGUA

# def f(x):
#   return 8.11 - math.sqrt(2*9.81*x) * math.tanh(((math.sqrt(2*9.81*x))/(2*8.74))*5.49)

# def df(x):
#   return - (3* math.sqrt(109)* math.tanh((1647*math.sqrt(109)*math.sqrt(x))/(2185*2**(5/2))))/(5*2**(3/2)*math.sqrt(x)) - (538569 * (1/(math.cosh((1647*math.sqrt(109)*math.sqrt(x))/(2185* 2**(5/2)))))**2)/174800

# numIteracao = 5
# x0 = 1.86

#################################

# ARQUIMEDES ESFERA

# def f(x):
#   r = 4.92
#   pw = 1000
#   ps = 76.01
#   v = (math.pi * x*x)/3 * (3*r - x)
#   vs = 4/3 * math.pi * r*r*r

#   return pw * (vs - v)- ps *vs


# def df(x):
#   r = 4.92
#   return 1000 *math.pi * x * (x - 2 * r)

# x0 = 4.69
# numIteracao = 5

###--####--####--####--####--##

# particula em repouso numa superfície plana

# def f(x):
#   g = 9.81
#   t = 1.43
#   d = 1.63
#   return ((math.sinh(x*t) - math.sin(x*t)) * - g/(2*x*x)) - d

# def df(x):
#   g = 9.81
#   t = 1.43
#   return (g * (t * math.cos(t*x) - t * math.cosh(t*x)))/2*x*x - (g*(math.sin(t*x) - math.sinh(t*x)))/x*x*x

# x0 = -1.92
# numIteracao = 5 
###--####--####--####--####--##

# caixa de papelao

def f(x):
  return (6000*x*x - 54420*x + 77119)/500

def df(x):
  return (12000*x - 54420)/500

x0 = 2.56
numIteracao = 5

###--####--####--####--####--##

#   ZERO DE FUNCAO
#           Metodo de Newton

# Entrada: estimativa inicial (x0), funcao (f), derivada funcao (df), e numero de iteracoes (numIteracao)
def metodoNewton(x0,f,df,numIteracao):
  print("Calcular metodo de Newton !!\n\n")
  for i in range(numIteracao):
    if(df(x0) == 0):
      print("Divisao por zero na derivada em {}\n".format(x0))
      break
    else:
      x0 = x0 - f(x0) / df(x0)
      print("x_{} = {}\n".format(i+1,x0))

if __name__ == "__main__":
  metodoNewton(x0,f,df, numIteracao)