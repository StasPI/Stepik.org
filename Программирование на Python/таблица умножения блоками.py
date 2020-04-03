a = int(input())
b = int(input())
c = int(input())
d = int(input())
print (end = '\t')
for i in range(c, d + 1):
    print(i, end = '\t')
print('\t')
for j in range(a, b + 1):
    print(j, end = '\t')
    for w in range(c, d + 1):
        print(w * j, end = '\t')
    print('\t')