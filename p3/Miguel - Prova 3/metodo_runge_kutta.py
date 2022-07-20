def rk4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * (m2 + m3) + m4) / 6
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r

#Q11 Prova:
def f(x,y):
    return y*(1-x)+x+2

x0, y0 = 0.89019, 1.18626
e = rk4(f,x0,y0, h=0.15664,n=10)
for xi, yi in e:
    print(xi, yi)