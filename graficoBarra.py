import matplotlib.pyplot as plt

x = [1,2,3,6]
y = [5,6,7,10]

x1 = [9,4,6,8]
y1 = [1,2,3,5]

eixox = "Eixo X"
eixoy = "Eixo Y"
titulo = "Gráfico de Barra"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.plot(x,y)
plt.bar(x,y, label="Grupo 1")
plt.bar(x1,y1, label="Grupo 2")
plt.legend()
plt.show()
