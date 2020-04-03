f = float(input())
s = float(input())
o = input("")
if (o == '/' or o == 'mod' or o == '%' or o == 'div' or o == '//') and s == 0:
    print("Деление на 0!")
elif o == '+':
    print(f + s)
elif o == '-':
    print(f - s)
elif o == '*':
    print(f * s)
elif o == '/':
    print(f / s)
elif o == 'mod' or o == '%':
    print(f % s)
elif o == 'pow' or o == '**':
    print(f ** s)
elif o == 'div' or o == '//':
    print(f // s)
