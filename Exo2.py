import re 
import sys

pattern = r'[5][6]'
p = re.compile(pattern)
with open (sys.argv[1]) as file :
    for i,line in enumerate(file):
        instances = p.findall(line)
        if len(instances) !=0:
            print ('Line{}: {}'.format(i+1, ', '.join(instances)))