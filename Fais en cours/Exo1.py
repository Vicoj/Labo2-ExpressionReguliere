import re

number = r'\+\d{2} \d{3} \d{2} \d{2} \d{2}'
entire = r'\+\d+|\-\d+'
plaque = r'\d[A-Z]{3}\d{3}'

p=re.compile(number)
z=re.compile(entire)
e=re.compile(plaque)

print(p.match('+34') is not None)
