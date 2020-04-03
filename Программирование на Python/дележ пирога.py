a = int(input())
b = int(input())
x1 = a
if a == b:
    print(a)
elif a % b == 0 or b % a == 0:
    if a > b:
        print(a)
    else:
        print(b)
else:
    while x1 % b != 0:
        x1 += a
        if x1 % b == 0:
            print(x1)
