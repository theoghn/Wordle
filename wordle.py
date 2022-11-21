import random
import runpy

f = open("Cuvinte.txt", "r")
cuvinte = f.readlines()
wr = open("Cuvinte_schimbate.txt", "w")
for cuv in cuvinte:
    wr.write(cuv)
chosen_word = random.choice(cuvinte).strip()
f.close()
wr.close()
print(chosen_word)


def test(x, word):
    v = [2, 2, 2, 2, 2]
    for i in range(5):
        if x[i] == word[i]:
            v[i] = 0
        elif x[i] in word:
            v[i] = 1
        else:
            v[i] = 2
    a = ""
    for prr in v:
        a += str(prr) + " "
    return a


f = open("communication.txt", "w+")
f.write("TAREI" + "\n")
print("TAREI")
f.write(str(test("TAREI", chosen_word))+"\n")
f.close()
runpy.run_path(path_name='tester.py')


def wordle():
    com = open("communication.txt", "r+")
    cuvant = str(com.readline()).strip()
    if cuvant == chosen_word:
        print(cuvant + " found")
        return 0
    else:
        print(cuvant)
    com.write(str(test(cuvant, chosen_word)))
    com.close()
    runpy.run_path(path_name='tester.py')
    wordle()

wordle()