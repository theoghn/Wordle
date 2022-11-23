import math
from time import time
before = time()


def culori(v):
    for x in v:
        if x == 0:
            print(green, end="")
        elif x == 1:
            print(yellow, end="")
        else:
            print(grey, end="")
    print()


def delete(v, variabila):
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



file = open("Cuvinte_schimbate.txt", "r")
cuvinte = file.read().split()
file.close()
nr_cuvinte = len(cuvinte)
unchanged_list = cuvinte.copy()

file = open("cazuri.txt", "r")
cazuri = file.read().split(";")

dict = {str(x): 0 for x in cazuri}

green = "\U0001F7E9"
yellow = "\U0001F7E8"
grey = "\u2B1B"

#print(entropy(tarei))
#culori(test(tarei,to_find))
def best():
    i = 0
    max = 0
    maxcuv = ""
    for x in cuvinte:
        i += 1
        b = entropy(x)
        if b > max:
            maxcuv = x
            max = b
    return maxcuv


f = open("solutii2.txt", "w")


incercari = 0
def solve():
    f = open("communication.txt", "r")
    folosit = f.readline().strip()
    caz = f.readline().split()
    v = [1, 1, 1, 2, 2]
    for r in range(5):
        v[r] = int(caz[r])
    #print(v)
    delete(v,folosit)

    wr = open("Cuvinte_schimbate.txt", "w+")
    for cuv in cuvinte:
        wr.write(cuv + "\n")
    wr.close()
    #print(nr_cuvinte)
    if nr_cuvinte != 1:
        alegere = best()
    else:
        alegere = cuvinte[0]
    f2 = open("communication.txt", "w+")
    f2.write(alegere + "\n")


solve()

# print(entropy(to_find))
#print(float(incercari/10))
#print(time()-before)
# SetUpdate(2)
