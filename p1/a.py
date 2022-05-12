from re import A

from pygame import K_7


fun = -7/5*4-6
print(fun)

# CRUZAMENTO    DENTRO          FORA
    #   A         x4 +  491   =    x3 + 467
    #   B         x3 + 588    =    x2 + 656
    #   C         566 + x2    =    547 + x1
    #   D         794 + x1    =    769 + x4

    #     #FLUXO QUE ENTRA = 2439
    #     # FLUXO QUE SAI = 2439

    #   x3 - x4 = 24 -> x4 = x3 - 24 > 0
    #   x3 - x2 = 68 -> x2 = x3 - 68 > 0
    #   x1 - x2 = 19 -> x1 = x3 - 49 > 0
    #   x4 - x1 = 25 -> x4 = 25 + x1

    # entra = k1 + k2 + k5 = 480,66666666666666666667
    # sai = k3 + k6 + x = 1442

k1=644
k2=461
k3=1382
k4=386
k5=337
k6=228

x1 = k1 + k2 - k7
x1 = k3 - x2
k5

x = k7 + x3 - k6


print(f'{k7} + {x3} = {x} + {k6}')
print(f'{k5 + k4} = {x2} + {x3}')
print(f'{x2} + {x1} = {k3}')
print(f'{k1 + k2} = {k7} + {x1}')