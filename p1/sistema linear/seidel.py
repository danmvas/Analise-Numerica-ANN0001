from jacobi import metodoJacobi
import math

#   SISTEMAS LINEARES
#           METODO DA ELIMINACAO DE GAUSS SEIDEL
# Entrada: matriz[lin][col], termosIndependentes[col], chute[col], numIteracao
# matriz é o sistema linear
# TI são as respostas em vetor do das equacoes do SL

def metodoGaussSeidel(matriz,ti,chute,numIteracao):
  linha=len(matriz)
  coluna=len(matriz[0])
  for it in range(numIteracao):
    for i in range(linha):
      xi = ti[i]
      for j in range(coluna):
        if i != j:
          xi -= matriz[i][j] * chute[j]
      xi /= matriz[i][i]
      chute[i] = xi
    #if it == 2 or it == 8 or it == 16:
    print("X^{} -> ".format(it+1))
    for k in range(coluna):
      print("{}".format(chute[k]))
    print("")

if __name__ == "__main__":

######################################
# QUESTÃO 27

  # A =[[-7.07,-4.53,1.42],
  #     [1.56,4.66,-1.98],
  #     [2.58,2.45,-6.15]]
  # B = [2.02, -3.72, 3.92]
  # chute = [-1.28,2.89,2.65]
  # n = 18

######################################
# QUESTÃO 28

  A =[[9.03,3.64,1.28,-3.08],
      [1.79,-4.68,1.24,0.61],
      [2.51,3.02,-9.78,3.22],
      [3.14,0.45,0.3,-4.94]]
  B = [-3.82, 3.02, -2.4, -0.77]
  chute = [1.15,4.88,-2.61,-0.52]
  n = 16

 #####################################
 #  
  # A = [[9.92398, 4.56492, -3.81009], [0.50034, 2.07938, 0.03008], [2.15027, 0.9574, -4.65664]]
  # B = [-0.98735, 2.34167, 0.56992]
  # chute = [1.07522, 2.65208, 3.90839]
  # n=18

  metodoGaussSeidel(A,B,chute,n)
