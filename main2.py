#!C:\Users\kumar\AppData\Local\Programs\Python\Python310\python.exe

import cgi


print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
pn=str(form.getvalue("username"))
print('<html>')
print('<body>')
print('<h1>%s<h1>'%pn)
print('</body></html>')