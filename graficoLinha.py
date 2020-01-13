import matplotlib.pyplot as plt

x = [1,2,3,6]
y = [5,6,7,10]

eixox = "Eixo X"
eixoy = "Eixo Y"
titulo = "Gráfico de Linha"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.plot(x,y)
plt.plot(x,y)
plt.show()

