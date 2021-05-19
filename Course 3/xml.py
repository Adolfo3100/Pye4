import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_895655.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

final = 0 
for i in range(len(counts)):
    lst = counts[i].text
    trans = int(lst)
    final = final + trans
print(final)