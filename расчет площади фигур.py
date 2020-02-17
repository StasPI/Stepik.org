ftype = input('')
if ftype == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif    ftype == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif    ftype == 'круг':
    r = float(input())
    p = 3.14
    s = p * (r * r)
    print(s)