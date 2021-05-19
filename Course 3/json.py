import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_895656.json'
uh = urllib.request.urlopen(url, context=ctx)

info = uh.read().decode()
js = json.loads(info)

final = 0
for i in js['comments']:
    almost = i['count']
    final = final + almost
print(final)