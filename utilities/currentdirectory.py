
import os

exampleText = ['hello','world']

# change directory to script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open('example.txt', 'w') as f:
    for x in exampleText:
        f.write(x +'\n')

print("Successfully saved into " + os.getcwd())


