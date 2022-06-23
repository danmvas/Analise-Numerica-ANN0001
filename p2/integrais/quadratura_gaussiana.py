
import math

#   INTEGRAIS
#           QUADRATURA GAUSSIANA

#(ponto x, peso c)

# n2 = [ (0.5773502692, 1.0000000000), (-0.5773502692, 1.0000000000)]
# n3 = [ (0.7745966692, 0.5555555556), (0.0000000000, 0.8888888889), (-0.7745966692, 0.5555555556) ]
# n4 = [ (0.8611363116, 0.3478548451), (0.3399810436, 0.6521451549), (-0.3399810436, 0.6521451549), (-0.8611363116, 0.3478548451) ]
# n5 = [ (0.9061798459, 0.2369268850), (0.5384693101, 0.4786286705), (0.0000000000, 0.5688888889), (-0.5384693101, 0.4786286704), (-0.9061798459, 0.2369268850) ]

#usar somente se o intervalo for de [-1, 1], caso não, usar mudanca
def quadratura(f, ponto_e_peso):
   soma = 0
   for x_k, c_k in ponto_e_peso:
      soma += c_k * f(x_k)
   return soma

#para integrais não definadas por intervalo [-1, 1] precisa fazer mudanca de variaveis
def mudanca(f, a, b, u):
  return f( ( b + a)/2 + ( b - a) * u /2) * ( b - a ) / 2

def f(x):
   return math.exp(-x**2)

a,b = -1.167, 1.228

def g(u):
   return mudanca(f,a,b,u)

pontos = (-0.33998104358485626, 0.33998104358485626, -0.8611363115940526, 0.8611363115940526)
pesos = (0.6521451548625461, 0.6521451548625461, 0.34785484513745385, 0.34785484513745385)
n4 = zip(pontos,pesos)
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P2.10
# def f(x):
#    return math.sin(x/math.sqrt((x**2) + 1)) + 1

# a,b = -1.44915, 1.38355

# def g(u):
#    return mudanca(f,a,b,u)

# pontos = (-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717)
# pesos = (0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814)
# n10 = zip(pontos,pesos)
#--------------------------------------------------------------------------


if __name__ == "__main__":
   print(quadratura(g,n4))
   print(quadratura(f,n4))
