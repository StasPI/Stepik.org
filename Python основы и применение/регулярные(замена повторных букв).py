'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:

attraction
buzzzz
Sample Output:

atraction
buz
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w*?)((\w)\3+)(\w*?)'
    result = re.sub(pattern, r'\1\3\4', line)
    print(result)
