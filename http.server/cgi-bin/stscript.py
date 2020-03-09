#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text = form.getfirst("INPUT_TEXT", "не задано")
text = text[:-1]

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>""")

for i in range(1, len(text) + 1, 2):
	print("<h1>" + str(hash(text[i])) + "</h1>")

print("""</body>
        </html>""")


# #!/usr/bin/env python3
# import cgi

# def ohash(s):
#     ans = 0
#     for c in s:
#         ans = ans * 123417 + ord(c)
#     return ans

# form = cgi.FieldStorage()
# text = form.getfirst("INPUT_TEXT", "не задано")

# print("Content-type: text/html\n")
# print("""<!DOCTYPE HTML>
#         <html>
#         <head>
#             <meta charset="utf-8">
#         </head>
#         <body>""")

# print("<h1>" + str(ohash(text)) + "</h1>")

# print("""</body>
#         </html>""")


# import cgi
# import html

# form = cgi.FieldStorage()
# substr = form.getfirst('INPUT_TEXT', 'не задано')

# fin = open(r'A:\learn\Python\__Test_Zone\server\gtp.tsv')
# lines = fin.readlines()
# fin.close()

# print("Content-type: text/html\n")
# print("""<!DOCTYPE HTML>
#     <html>
#     <head>
#         <meta charset="utf-8">
#         <title>Обработка данных форм</title>
#     </head>
#     <body> """)
# print('<table>')
# for line in lines:
#     data = line.split('\t')
#     name, gdp = data[1:3]
#     if substr in name:
#         print('<tr><td>', name, '</td><td>', gdp, '</td></tr>')
# print('</table>')

# print("""</body>
#         </html>""")
