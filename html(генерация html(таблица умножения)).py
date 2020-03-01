'''
В этой задаче вам необходимо научиться генерировать html-код на питоне и сдать на проверку html-файл, в котором 
будет таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10. При открытии 
вашего файла в браузере это должно выглядеть примерно так:
Ваш файл должен начинаться с тегов <html> и <body> и заканчиваться </body> и </html>.
Для создания таблицы можно пользоваться тегами <table> (создание таблицы), <tr> (создание строки в таблице) и 
<td> (создание отдельной ячейки). Все открытые теги нужно закрыть, причем сделать это нужно в правильном порядке.
Пожалуйста, не используйте никаких украшений и других тегов - мы не сможем проверить такие решения.
'''


from xml.etree import ElementTree as ET

number = int(input("Введите число:"))

html = ET.Element('html')
body = ET.Element('body')
html.append(body)
table = ET.Element('table')
body.append(table)


multiplication_table = [
    [i * j for i in range(1, number+1)] for j in range(1, number+1)]

for line in multiplication_table:
    tr = ET.Element('tr')
    table.append(tr)
    for element in line:
        td = ET.Element('td')
        tr.append(td)
        td.text = str(element)

ET.ElementTree(html).write('A:\\task\\new.html',
                           encoding='unicode', method='html')
