import math
def entropy(word):
    for x in cuvinte:
        for i in range(5):
            if x[i] == word[i]:
                v[i] = 0
            elif x[i] in word:
                v[i] = 1
            else:
                v[i] = 2
        if str(v) in dict:
            dict[str(v)] += 1

    s = 0
    t = 11454
    for x in dict:
        c = int(dict[x])
        p = c/t
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
v = [0, 0, 0, 0, 0]
tarei = "TAREI"
caz = [1, 2, 1, 1, 1]

green = "\u1F7E9"
yellow = "\u1F7E8"
grey = "\u2B1B"

print(entropy(tarei))
set = {x for x in cuvinte}
SetUpdate(2)
