import matplotlib.pyplot as plt

x = [1,5,3,6]
y = [5,10,7,10]

eixox = "Eixo X"
eixoy = "Eixo Y"
titulo = "Scatterplot: Gráfico de dispersão"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x,y, label="Meus Pontos", color ='y')
plt.plot(x,y) #linhas
plt.legend()
plt.show()

plt.savefig("GraficoDePonto.png", dpi=300)
