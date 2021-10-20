from numpy import linspace
from matplotlib import pyplot as plt

# La conclusión es que casi es mejor cogiendo un número del intervalo y ya está, ALV

# Los resultados son independientes de las cuotas (mientras cumplan la condición claro) ya que son constantes lineales
x = 1
c1 = 2.5
c2 = 1.67

dinero_y = list(linspace(x/(c2-1), x*(c1-1), 1000))


def beneficio_y(y):
    return y*(c2-1)-x


def beneficio_x(y):
    return x*(c1-1)-y


resultados_y = [beneficio_y(y) for y in dinero_y]
resultados_x = [beneficio_x(y) for y in dinero_y]

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Vertically stacked subplots')
ax1.plot(dinero_y, resultados_y)
ax1.set_title("Resultados y")
ax2.plot(dinero_y, resultados_x)
ax2.set_title("Resultados x")

# De aquí vemos que cuánto más aumenta el dinero puesto en y, más ganamos si gana y pero menos ganamos si gana x (esto siempre que c1 sea mayor que c2, si no es al revés), vamos a calcular el valor esperado suponiendo que los dos sucesos son equiprobables (si quisiésemos hacerlo mejor en vd como los sucesos no son equiprobables habría que, en vez de hacer la medi aritmética, asinarle un peso a cada uno (obviamente será más probable el de menor cuota))

media = [(x + y)/2 for x, y in zip(resultados_x, resultados_y)]
ax3.plot(dinero_y, media)
ax3.set_title("Resultados medios")
plt.show()
