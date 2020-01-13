#Crescimento da População Brasileira 1980 -2016

import matplotlib.pyplot as plt

date = open("populacao-brasileira.csv").readlines()

x=[]
y=[]

for i in range(len(date)):
    if i != 0:
        linha = date[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x,y)
plt.show()
