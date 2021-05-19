from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
final = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tacos = str(soup)
stuff = re.findall('[0-9]+', tacos)

del stuff[0:4]

for i in stuff:
    final = final + int(i)
    
print(final)

#http://py4e-data.dr-chuck.net/comments_42.html