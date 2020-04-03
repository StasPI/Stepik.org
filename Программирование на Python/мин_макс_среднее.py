a = int(input())
b = int(input())
c = int(input())
x = [a, b, c]
if b <= a <= c or c <= a <= b:
    print(max(x))
    print(min(x))
    print(a)
elif a <= b <= c or c <= b <= a:
    print(max(x))
    print(min(x))
    print(b)
else:
    print(max(x))
    print(min(x))
    print(c)