def heun(f,x0,y0,h,n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h *(m1 + m2) / 2
        x0 += h
        y0 = y1
        r.append((x0,y0))
    return r

#Q9 Prova:
def f(x,y):
    return y*(2-x)+x+1

x0, y0 = 0.80961, 1.29188
e = heun(f,x0,y0, h=0.19585,n=10)
for xi, yi in e:
    print(xi, yi)