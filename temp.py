f = open("Cuvinte.txt", "r")
cuvinte = f.readlines()
wr = open("Cuvinte_schimbate.txt", "w")
for cuv in cuvinte:
    wr.write(cuv)