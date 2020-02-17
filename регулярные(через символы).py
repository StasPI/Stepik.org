'''
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:
zabcz
zzxzz
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'z.{3}z'
    result = re.findall(pattern, line)
    if len(result) > 0:
        print(line)
