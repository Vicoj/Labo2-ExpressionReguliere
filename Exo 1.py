import re
numero=input('Encoder le numero :')
number = r'\+\d{2} \d{3} \d{2} \d{2} \d{2}'
entire = r'\+\d+|\-\d+'
plaque = r'\w\d[A-Z]{3}\w{3}'

p=re.compile(number)
z=re.compile(entire)
e=re.compile(plaque)

if p.match(numero) is not None :
    print('Le numero est encode')
if z.match(numero) is not None :
    print('Lentier est encode')
if e.match(numero) is not None :
    print('La plaque est encode')
else : 
    print('Maivais encodage réessayer ')