
import cgi
import html

form = cgi.FieldStorage()
substr = form.getfirst('INPUT_TEXT', 'не задано')

fin = open(r'A:\learn\Python\__Test_Zone\server\gtp.tsv')
lines = fin.readlines()
fin.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Обработка данных форм</title>
    </head>
    <body> """)
print('<table>')
for line in lines:
    data = line.split('\t')
    name, gdp = data[1:3]
    if substr in name:
        print('<tr><td>', name, '</td><td>', gdp, '</td></tr>')
print('</table>')

print("""</body>
        </html>""")
