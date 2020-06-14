## EXPRESSION REGULIERE
import re
#Exemple : Numéro de téléphone
pattern = r'[0-9]{4}/[0-9]{2}\.[0-9]{2}\.[0-9]{2}'
p = re. compile ( pattern )

#print (p. match ('0394/83.31.41'))
#print (p. match ('0394/83-31-41'))


# Précéder les méta-caractères avec un backslash
# . ^ $ * + ? { } [ ] \ | ( )

# Classes de caractères définies avec les [ ]
# [abc] : a, b ou c
# [0-9] : n'importe quoi entre 0 et 9
# [a-zA-Z] : n'importe quoi entre a et z ou entre A et Z
# [^aeiou] : n'importe quoi sauf a, e, i, o ou u
# [a-z&&[^b]] : intersection entre deux ensembles

# Classes prédéfinies de caractères
# . : n'importe quel caractère (sauf retour à la ligne)
# \d : un chiffre (équivalent à [0-9])
# \s : un caractère blanc (équivalent à [ \t\n\r\f\v])
# \w : un caractère alpha-numérique (équivalent à [a-zA-Z0-9_])

# Répétitions d'occurrences avec une quantificateur
# {n} : exactement n occurrences
# {m,n} : au moins m et au plus n occurrences
# {m,} : au moins m occurrences
# {,n} : au plus n occurrences
 
# Quantificateurs prédéfinis
# ? = {0,1}
# * = {0,}
# + = {1,}
 
# Frontières de recherche
# ^ : début de la ligne
# $ : fin de la ligne

#Exemple : Nombre entier
pattern = r'-?[1-9][0-9]*'
p = re.compile(pattern)

#print (p. match ('15') is not None ) # True
#print (p. match ('03') is not None ) # False
#print (p. match ('-7') is not None ) # True
#print (p. match ('-42') is not None ) # True
#print (p. match ('8 enfants!') is not None ) # True

#Vérifier une chaine (2)
pattern = r'-?[1-9][0-9]*'
m = re.compile(pattern)

print (m.match('8 enfants !') is not None ) # False

#Options de compilation
# Flags à passer à la méthode compileµ
# re.IGNORECASE Recherche insensible à la casse
# re.DOTALL Le point matche également les retours à la ligne
# re.MULTILINE Les matches peuvent se faire sur plusieurs lignes

pattern = r'^[a-z]+$'
p = re.compile(pattern,re.IGNORECASE)

print (p.match ('bogoss') is not None ) # True
print (p.match ('LaTeX') is not None ) # True