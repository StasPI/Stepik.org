a = int(input())
b = int(input())
s = 0
s1 = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        s1 += 1
print(s / s1)