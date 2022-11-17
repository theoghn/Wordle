import math
from time import time
before = time()
def culori(v):
    for x in v:
        if x == 0:
            print(green,end="")
        elif x == 1:
            print(yellow,end="")
        else:
            print(grey,end="")

def entropy(word):
    for x in dict:
        dict[x] = 0
    for x in cuvinte:
        v = [2, 2, 2, 2, 2]
        a = ""
        for i in range(5):
            if x[i] == word[i]:
                v[i] = 0
                a += x[i]
        for i in range(5):
            if v[i] == 0:
                continue
            elif x[i] in word and word.count(x[i]) > a.count(x[i]):
                v[i] = 1
                a += x[i]
            else:
                v[i] = 2
        if str(v) in dict:
            dict[str(v)] += 1
            print(x)
            culori(v)
            print()
        else:
            dict[str(v)] = 1
            print(v)
            print("error")

    s = 0
    t = 11454
    for x in dict:
        c = float(dict[x])
        p = c/t
        if p!= 0:
            s += p*math.log2(1/p)
    return s


def SetUpdate(caz):
    for x in cuvinte:
        print("maine")

file = open("cuvinte.txt","r")
cuvinte = file.read().split()

file = open("cazuri.txt","r")
cazuri = file.read().split(";")

dict = {str(x): 0 for x in cazuri}

tarei = "TAREI"
caz = [1, 2, 1, 1, 1]

green = "\U0001F7E9"
yellow = "\U0001F7E8"
grey = "\u2B1B"

print(entropy(tarei))
set = {x for x in cuvinte}
i = 0
max = 0
maxcuv = "ar"
'''
for x in set:
    i += 1
    if(i % 100==0):
        print (i)
    b = entropy(x)
    if b > max:
        maxcuv = x
        max = b
'''
print(max)
print(maxcuv)

print(time()-before)
#SetUpdate(2)
