import math

# Functie pentru stergerea cuvintelor in functie de patternul primit
def delete(pattern, guess):
    global nr_cuvinte
    cuvinte2 = cuvinte.copy()
    for cuvant in cuvinte2:
        for i in range(5):
            if pattern[i] == 0 and guess[i] != cuvant[i]:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break
            elif pattern[i] == 1 and guess[i] not in cuvant:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break
            elif pattern[i] == 1 and guess[i] == cuvant[i]:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break
            elif pattern[i] == 2 and guess[i] in cuvant:
                nr_cuvinte -= 1
                cuvinte.remove(cuvant)
                break

# Functie pentru calcularea entropiei
def entropy(word):
    # reintializare dictionarului cu valori de 0
    for x in dict:
        dict[x] = 0
    # completarea dictionarului de cazuri cu nr de aparitii al fiecaruia
    for cuvant in cuvinte:
        v = [2, 2, 2, 2, 2]
        for i in range(5):
            if cuvant[i] == word[i]:
                v[i] = 0
            elif word[i] in cuvant:
                v[i] = 1
            else:
                v[i] = 2
        if str(v) in dict:
            dict[str(v)] += 1

    #calcularea entropiei cuvantului
    s = 0
    for x in dict:
        c = float(dict[x])
        p = c/nr_cuvinte
        if p != 0:
            s += p*math.log2(1/p)
    return s


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

# Funtia alege cuvantul cu cea mai buna entropie
def best():
    max = 0
    maxcuv = ""
    for cuvant in cuvinte:
        var = entropy(cuvant)
        # Evita cateva cazuri in care mai multe cuvinte au aceasi entropie si trebuie sa ajunga la ultimul
        if var > max:
            maxcuv = cuvant
            max = var
    return maxcuv

# Functia principala
def solve():
    f = open("communication.txt", "r")
    folosit = f.readline().strip()
    caz = f.readline().split()
    # solutie pentru a evita cateva erori in compararea '2'si 2
    v = [1, 1, 1, 2, 2]
    for r in range(5):
        v[r] = int(caz[r])
    # sterge cuvintele care nu mai pot fi posibile
    delete(v,folosit)

    # updatam lista de cuvinte
    wr = open("Cuvinte_schimbate.txt", "w+")
    for cuv in cuvinte:
        wr.write(cuv + "\n")
    wr.close()
    # cand in lista ramane un sigur cuvant apar erori evitate astfel
    if nr_cuvinte != 1:
        alegere = best()
    else:
        alegere = cuvinte[0]
    f2 = open("communication.txt", "w+")
    f2.write(alegere + "\n")


solve()