import math

####--####--####--####--####--##
#Exercise 22

# def f(x):
#   return x - 2**-x

# a = 0.1748
# b = 1.0782
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 23

# def f(x):
#   return x**2 - 3

# a = -2.3751
# b = -0.55
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 24

# def f(x):
#   return x**2 - 7

# a = 2.1968
# b = 3.3658
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 25

# def f(x):
#   return x**3 - 7*x**2 + 14*x - 7

# a = 0.1992
# b = 4.0556
# numIteracao = 5
####--####--####--####--####--##
####--####--####--####--####--##
#Exercise 26

# def f(x):
#   return 2*(x+1)*(x-0.5)*(x-1)

# a = -1.6892
# b = 1.3087
# numIteracao = 5
####--####--####--####--####--##
###--####--####--####--####--##
# Exercise 28

# def f(x):
#   return math.e**(5*x) - 2
# a=-0.90057
# b=1.9895
# numIteracao = 6400
###--####--####--####--####--##

###--####--####--####--####--##
# PROVA - 4

#def f(x):
#  return 2*(x+1)*(x-0.5)*(x-1)

# def f(x):
#   return 1000*((math.pi*(2.14-x))/3.0)*(pow((2.16+x*(5.72-2.16)/2.14),2)+pow(5.72,2) + (2.16+x*(5.72-2.16)/2.14)*5.72) - 553.01*((math.pi*2.14)/3.0)*(pow(2.16,2)+pow(5.72,2) + 2.16*5.72)

# a=0
# b=2.14

###--####--####--####--####--##

# def f(x):
#   return 1586191*(math.e)**x + (219635/x)*(math.e**(x)-1) - 3406533

# a = 0.1
# b = 1.78
# numIteracao = 11

def f(x):
  return ((9.81/27.42)*x * (1 - exp(-(27.42/x)*9.58)) - 38.26);

###--####--####--####--####--##

#   ZERO DE FUNCAO
#           METODO DA POSICAO FALSA
# Entrada: intervalo (a) e (b), funcao (f) numero de iteracoes (numIteracao)
def metodoFalsaPosicao(a, b, f, numIteracao):
  fa = f(a)
  fb = f(b)
  print("Calcular metodo da posição falsa !!\n\n")
  if (fa * fb >= 0):
    print("Não sabe-se se a função possui raiz no intervalo [{},{}]\n".format(a,b))
    return False
  else:
    for i in range(numIteracao):
      x = (a*fb - b*fa)/(fb - fa)
      print("x_{} = {}\n".format(i + 1,x))
      fx = f(x)
      if(fx == 0):
        print("A raiz é {}\n".format(x))
        return
      if (fa * fx < 0):
        b = x
        fb = fx
      else:
        a = x
        fa = fx

if __name__ == "__main__":
  metodoFalsaPosicao(a, b, f, numIteracao) 