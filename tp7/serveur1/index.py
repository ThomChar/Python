# -*- coding: UTF-8 -*-

import cgi 

import sys
import codecs

# print with utf-8 
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8\n")

print("<!DOCTYPE html>")
header = """
<head>
    <title>Mon programme</title>
    <meta charset="utf-8" />
</head>
"""
print(header)

print("""<body>""")

print(form.getvalue("name"))

print("""
<form action="/index.py" method="post" accept-charset="UTF-8">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
    """)

print("""</body>
</html>""")