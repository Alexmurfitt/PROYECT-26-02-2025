import matplotlib
matplotlib.use('Agg')  # Prueba con este backend
import matplotlib.pyplot as plt

print("El script visualization.py se está ejecutando correctamente")

# Prueba un gráfico simple
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("prueba.png")  # Guarda el gráfico en un archivo
print("Gráfico guardado como prueba.png")




