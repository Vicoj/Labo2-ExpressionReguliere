#import re

#with open('number.txt') as file:
#    n = (file.readlines())
#print(n)
#p = re.compile(r'\d+')
#line=1
#for i in n:
#    z = p.findall(i)
#    if len(z)>0:
#        s='line '+str(line)+' : '
#        for nb in z:
#            s+=nb+', '
#        print(s)
#    line+=1

#correction
import re
import sys 

pattern = r'\d+'
p = re.compile(pattern)

with open(sys.argv[1]) as file :
    for i, line in enumerate(file):
        instances  = p.findall(line)
        if len(instances) !=0:
            print('Line {}: {}'.format(i+1, ', '.join(instances)))
