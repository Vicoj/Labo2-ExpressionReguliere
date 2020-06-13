import re
pattern = r'\d+'
p = re.compile(pattern)
m = p.match('72 est égal à 70 + 2')
if m is not None:
    print(m.group()) # 72

print(p.findall(’72 est égal à 70 + 2’))
