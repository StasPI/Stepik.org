'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
Примечание:
Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации.
Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?
Sample Output:
cat
catapult and cat
"cat"
!cat?
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\bcat\b'
    result = re.findall(pattern, line)
    if len(result) > 0:
        print(line)
