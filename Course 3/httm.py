import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for w in range(7):
    if w == 0:
        url = input('Enter - ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
    else:
        url = 'http://py4e-data.dr-chuck.net/known_by_'+ names[0] + ".html"
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
    i = 0
    names = []
    for tag in tags:
        if i == 17:
            h = str(tag)
            names = (re.findall(
                '^<a href="http://py4e-data.dr-chuck.net/known_by_([A-Za-z]+)',h))
            break
        else:
            i = 1 + i

print(names)
#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#http://py4e-data.dr-chuck.net/known_by_Jean.html