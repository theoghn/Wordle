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
print(chosen_word + " - To Find \n")

# Functia intoarce patternul de culori (2 = gri ,1 = galben ,0 = verde)
def test(guess, word):
    v = [2, 2, 2, 2, 2]
    for i in range(5):
        if guess[i] == word[i]:
            v[i] = 0
        elif guess[i] in word:
            v[i] = 1
        else:
            v[i] = 2
    pattern = ""
    for value in v:
        pattern += str(value) + " "
    return pattern


f = open("communication.txt", "w+")
f.write("TAREI" + "\n")
print("TAREI")
f.write(str(test("TAREI", chosen_word))+"\n")
f.close()
runpy.run_path(path_name='tester.py')

# Functie apelata recursiv pana la identificare cuvatului
def wordle():
    com = open("communication.txt", "r+")
    cuvant = str(com.readline()).strip()
    if cuvant == chosen_word:
        print(cuvant + " - Found")
        return 0
    else:
        print(cuvant)
    com.write(str(test(cuvant, chosen_word)))
    com.close()
    runpy.run_path(path_name='tester.py')
    wordle()

wordle()