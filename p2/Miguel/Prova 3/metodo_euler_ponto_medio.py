def euler(f, x0, y0, h, n):
    r = []
    for i in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + (h/2), y0 + (h/2) * m1)
        yk = y0 + h * m2
        y0 = yk
        x0 += h
        r.append((x0, y0))
    return r

#Q8 Prova:
def f(x,y):
    return y*(2-x)+x+1

x0 = 1.23883
y0 = 2.39759
e = euler(f, x0, y0, h=0.17864, n=10)
for xi, yi in e:
    print(xi, yi)