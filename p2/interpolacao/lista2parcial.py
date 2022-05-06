import math

from matplotlib.pyplot import xkcd

#   O método da eliminação de Gauss para resolver sistemas lineares consiste em transformar a matriz dos coeficientes de um SL num matriz triangular superior

#--------------------------------------------------------------------------
#EX 5
# def f(x):
#   return math.cos(x)**3 + 2*math.cos(x)**2 + 1
# x = [-2.088, -1.172, 0.389, 1.692, 2.545, 4.072]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 6
# def f(x):
  # return math.e**(-x**2) + math.cos(x) + 3
#x = [0.509, 0.93, 1.493, 2.502, 3.38, 3.847, 4.565, 5.187, 6.19, 6.683]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 7
# def p(x):
#   return x**2 * 81443750/334585449 - x * 4436736643/1338341796 + 2617870059479/223056966000
# x = [3.073, 3.766]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 8
# def p(x):
#   return x**4*0.14023273648 + x**3*0.21772723987 \
#   - x**2* 1.2616519467 - x*0.68065594597 + 3.67973722706
# x = [-0.019, 0.569, 2.389]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 9
# def p(x):
#   return \
#     x**8*0.18387353392 - x**7*2.65110966837 \
#   + x**6*16.3799285716 - x**5*56.3523304791 \
#   + x**4*116.979447767 - x**3*147.507235005 \
#   + x**2*107.039311547 - x**1*38.914031491 \
#   + 5.84173543731
# x = [0.482, 0.867, 1.982, 2.486, 2.766, 2.928]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 10
# def f(x):
#   return math.cos(x)**3 + 2*math.cos(x)**2 + 1

# def p(x):
#   return x**2*0.17906484299 - x*0.09492844951 \
#   + 0.88798745653

# def erroAbs(x):
#   return abs(f(x) - (p(x)))

#x = [-1.223, 1.365, 2.482]
#x = [2.688, 3.41]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 11
# def f(x):
#   return 1/(1+25*x**2)

# def p(x):
#   return x**4*10.9489846985 + x**3*0.60986042411 \
#   - x**2*7.63719475749 + x*0.32665150039 + 0.97196548561

# def erroAbs(x):
#   return abs(f(x) - (p(x)))

#x = [-0.807, -0.279, -0.054, 0.4, 0.652]
#x = [-0.588, 0.808, 0.943]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 12
# def f(x):
#   return math.cos(math.sin(math.log(x**2)))

# def p(x):
#   return x**8*0.19525801392 - x**7*2.87566999599 \
#     + x**6*18.1050363058 - x**5*63.3525459364 \
#     + x**4*133.670665401 - x**3*171.651630371 \
#     + x**2*127.80952033 - x*48.6420081069 \
#     + 7.74145115876

# def erroAbs(x):
#   return abs(f(x) - (p(x)))

#x = [0.473, 0.715, 0.983, 1.39, 1.624, 1.917, 2.146, 2.634, 2.919]
#x = [0.304, 1.15, 1.171, 1.256, 1.689, 2.132]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 16
# def f(x):
#   return math.sin(x)**4 - 4*math.sin(x)**2 \
#     + math.cos(x**2) + math.e**(-x**2) + 5

# x = [2.333, 3.44, 5.11]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 17
# def f(x):
#   return math.cos(x)**3 + 2*math.cos(x)**2 + 1

# x = [-2.27, -1.429, 0.059, 1.075, 1.53, 2.741, 3.659]

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 18
# def f(x):
#   return math.cos(x+math.sqrt(math.log(x**2)))

# x = [1.659, 1.868, 2.246, 2.673, 2.783, 3.311, 3.535, 3.802, 4.162, 4.602, 4.897]
# y = [-0.8886530272424157, -0.9879068771831346, -0.9299453170701573,
#      -0.5948701546736543, -0.478226574414906, 0.14550995077127812, 0.4002321028257195,
#      0.6623469949725336, 0.9079621022211206, 0.9978166431804776, 0.9224964353247108]

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 22
# def f(x):
#   return math.sin(x)**3 - 3*math.sin(x)**2 \
#   + math.sin(x**2) + 4

# x = [-3.383, -0.549, 3.507]
# y = [2.9413694624918048, 3.3378234280827916, 3.307171660210332]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 23
# def f(x):
#   return x**5 - 4*x**2 + 2*math.sqrt(x+1) + math.cos(x)

# x = [-0.264, -0.078, 0.244, 0.573, 0.705, 1.118, 1.466]
# y = [2.4010963861639714, 2.8930372762721377,
#      2.9637952217763894,2.0971175892850598,
#      1.5591833878928063, 0.09511838701012021,
#      1.4199468110458815]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 24
# def f(x):
#   return 1 / (1 + 25*x**2)

# x = [-0.899, -0.658, -0.586, -0.299, -0.153, -0.021, 0.23, 0.355, 0.563, 0.76, 0.937]
# y = [0.047158633389962984, 0.08457303304268401,
#      0.10433077027407694, 0.3091166219735551,
#      0.6308252771688562, 0.9890952251428006,
#      0.4305705059203445, 0.24092757114892338,
#      0.1120545481540414, 0.06476683937823835,
#      0.04357445621802043]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 28
# def f(x):
#   return math.cos(x+math.sqrt(math.log(x**2)))
# x = [2.124, 2.396, 3.536, 4.445]
# y = [-0.97806329798541, -0.8384431421779805,
#      0.4013113368675073, 0.9938583430896663]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 29
# def f(x):
#   return math.e**(math.cos(x)**2) + math.e**(-x**2) + math.log(x)
# x = [1.406, 2.843, 3.489, 5.24, 6.216, 6.904, 8.74]
# y = [1.5065338642621993, 3.538103904069116,
#      3.670391556879209, 2.944826608344334,
#      4.533184501315814, 3.870044539582267,
#      3.989924091312181]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 30
# y = []
# def f(x):
#   return math.e**(-x**2) + math.cos(x) + 3
# x = [0.294, 0.832, 1.355, 2.022, 2.539, 2.845, 3.617, 4.197, 4.712, 5.238, 5.475, 5.98, 6.652]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P2.2
# def f(x):
#   return x**5 - 4*x**2 + 2*math.sqrt(x+1) + math.cos(x)
# y = [1.8099749372185823, 2.6866480011948664, 2.9086969688012188, 2.496042790430524, 1.2995519585320157, 0.08740210414263955, 0.11144330455286494]
# x = [-0.402, -0.172, 0.282, 0.457, 0.765, 1.124, 1.247]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P1.1
# def f(x):
#   return 1/(1+25*x**2)

# def p(x):
#   return +0.04858938929211333*((x+0.282)*(x+0.106)*(x-0.316)*(x-0.642))/((-0.885+0.282)*(-0.885+0.106)*(-0.885-0.316)*(-0.885-0.642))+0.33466082125765545*((x+0.885)*(x+0.106)*(x-0.316)*(x-0.642))/((-0.282+0.885)*(-0.282+0.106)*(-0.282-0.316)*(-0.282-0.642))+0.7807010695604654*((x+0.885)*(x+0.282)*(x-0.316)*(x-0.642))/((-0.106+0.885)*(-0.106+0.282)*(-0.106-0.316)*(-0.106-0.642))+0.2860084658505892*((x+0.885)*(x+0.282)*(x+0.106)*(x-0.642))/((0.316+0.885)*(0.316+0.282)*(0.316+0.106)*(0.316-0.642))+0.08846347785316831*((x+0.885)*(x+0.282)*(x+0.106)*(x-0.316))/((0.642+0.885)*(0.642+0.282)*(0.642+0.106)*(0.642-0.316))

# def erroAbs(x):
#   return abs(f(x) - (p(x)))

# y = [0.04858938929211333, 0.33466082125765545, 0.7807010695604654, 0.2860084658505892, 0.08846347785316831]
# x = [-0.885, -0.282, -0.106, 0.316, 0.642]
# value = [-0.314, -0.126, 0.939]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P3.3
def f(x):
  return math.cos(x**2) + x**2 + math.e**-(x**4)

x = [-1.65722, 1.95035]
#--------------------------------------------------------------------------


if __name__ == "__main__":
  # for i in range(len(x)):
  #   y.append(f(x[i]))
  # print(y)
  # print(x)
  # for i in range(len(value)):
  #   print(value[i],erroAbs(value[i]))
  for i in range(2):
    print(f(x[i]))




