##Exemple Lambda
bytwo = lambda n : n*2
#print(bytwo(2)) 

##Exemple Fonction map
data = [1,2,3]
result = map(lambda x : x**2,data)
#print (list(result))

##Example Fonction filter
data = [1,-2,0,7,-3]
result = filter(lambda x : x>=0,data)
#print (list(result))

##Example Fonction filter
data = [2+1j,-1j,4]
#print (sum(data))

##Example Fonction reduce
from functools import reduce
L = [1,2,3,4]
print (reduce(lambda S, elem : S+elem,L,0))