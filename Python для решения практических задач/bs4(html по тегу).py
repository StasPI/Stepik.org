'''
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про 
язык Python. В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам 
нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые 
встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.
Например, если исходный текст страницы выглядел бы так:
<code>a</code>
<a>bracadabr</a>
<code>c</code>
<code>b</code>
<code>b</code>
<code>c</code>
то в ответ надо было бы ввести строку "b c".
'''

from collections import Counter
from bs4 import BeautifulSoup
import requests

html = requests.get(
    'https://stepik.org/media/attachments/lesson/209719/2.html')

tag_text = []
count = 0
finish = []

soup = BeautifulSoup(html.text, 'lxml')
for tag in soup.find_all('code'):
    tag_text.append(tag.text)

c = Counter(tag_text)

for element in c.items():
    if count < element[1]:
        count = element[1]

for element in c.items():
    if count == element[1]:
        finish.append(element[0])
finish.sort()
print(*finish)
