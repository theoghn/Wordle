import copy
import math
file = open("cuvinte.txt","r")
cuv = file.read()
cuvinte = cuv.split()

file = open("cazuri.txt","r")
p = file.read()
cazuri = p.split(";")

dict = {str(x): 0 for x in cazuri}
print (dict)

nr = 0
v = [0, 0, 0, 0, 0]
variante = [[0, 0, 0, 0, 0], [2, 2, 2, 2, 0]]
tarei = "TAREI"

for x in cuvinte:
    print(x)
    for i in range(5):
        if x[i] == tarei[i]:
            v[i] = 0
        elif x[i] in tarei:
            v[i] = 1
        else:
            v[i] = 2
    if str(v) in dict:
        dict[str(v)] += 1
    else:
        dict[str(v)] = 1
s = 0
t = 11454
s2 = 0
for x in dict:
    c = int(dict[x])
    p = c/t
    s += p*math.log2(1/p)
print(s)
