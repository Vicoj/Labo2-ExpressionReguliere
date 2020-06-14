import re
lien = "http://www.this.is/big/shit"
pattern = r'^(?P<protocole>[a-z]+)://(?P<domain>[^/])/(?P<path>[.]+)$'
p = re.compile(pattern)
words = p.match(lien)
if words is not None :
    print(words.groups())
pattern = r'^(?P<pseudo>[a-z]+)@(?P<domain>[a-z]+)\.(?P<extension>[a-z]{2,3})$'
p = re.compile(pattern)

m = p.match('email@example.net')
if m is not None :
    print (m.groups())
    print (m.group(1))
    print (m.group('domain'))