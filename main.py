import math
from time import time
before = time()

nr_cuvinte = 11454
def culori(v):
    for x in v:
        if x == 0:
            print(green, end="")
        elif x == 1:
            print(yellow, end="")
        else:
            print(grey, end="")
    print()

def delete(v,variabila):
    global nr_cuvinte
    cuvinte2 = cuvinte.copy()
    for cuvant in cuvinte2:
        for i in range(5):
            if v[i] == 0 and variabila[i] != cuvant[i]:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break
            elif v[i] == 1 and variabila[i] not in cuvant:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break
            elif v[i] == 1 and variabila[i] == cuvant[i]:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break
            elif v[i] == 2 and variabila[i] in cuvant:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break


def entropy(word):
    for x in dict:
        dict[x] = 0
    for x in cuvinte:
        v = test(x, word)
        if str(v) in dict:
            dict[str(v)] += 1
            '''print(x)
            culori(v)
            print()'''
    s = 0
    for x in dict:
        c = float(dict[x])
        p = c/nr_cuvinte
        if p != 0:
            s += p*math.log2(1/p)
    return s


def test(x, word):
    v = [2, 2, 2, 2, 2]
    for i in range(5):
        if x[i] == word[i]:
            v[i] = 0
        elif x[i] in word:
            v[i] = 1
        else:
            v[i] = 2
    return v


def SetUpdate(caz):
    for x in cuvinte:
        print("maine")


file = open("cuvinte.txt", "r")
cuvinte = file.read().split()
unchanged_list = cuvinte.copy()

file = open("cazuri.txt", "r")
cazuri = file.read().split(";")

dict = {str(x): 0 for x in cazuri}


caz = [1, 2, 1, 1, 1]


green = "\U0001F7E9"
yellow = "\U0001F7E8"
grey = "\u2B1B"

#print(entropy(tarei))
#culori(test(tarei,to_find))
def best():
    i = 0
    max = 0
    maxcuv = "ar"
    for x in cuvinte:
        i += 1
        b = entropy(x)
        if b > max:
            maxcuv = x
            max = b
    return maxcuv


f = open("solutii2.txt", "w")


incercari = 0
for to_find in unchanged_list:
    f.write(to_find + " ")
    tarei = "TAREI"
    f.write("TAREI ")
    culori(test(tarei,to_find))
    delete(test(tarei,to_find),tarei)
    print(nr_cuvinte, end=" ")
    print(tarei)
    incercari += 1
    while nr_cuvinte != 1:
        pl = best()
        incercari += 1
        delete(test(pl,to_find),pl)
        if nr_cuvinte != 1:
            f.write(pl + " ")
            print(pl)
        print(nr_cuvinte, end=" ")


    print(cuvinte[0])
    f.write(cuvinte[0] + "\n")

    cuvinte = unchanged_list.copy()
    nr_cuvinte = 11454

# print(entropy(to_find))
print(float(incercari/11454))
print(time()-before)
# SetUpdate(2)
