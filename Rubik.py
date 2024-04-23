import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from examples import r_up, r_down, l_up, l_down, d_left, d_right, u_left, u_right, f_right, f_left, b_right, b_left

# Definir los colores de cada cara del cubo de Rubik
colores = {
    1: 'yellow',       # Cara frontal
    2: 'white',    # Cara trasera
    3: 'green',     # Cara izquierda
    4: 'blue',      # Cara derecha
    5: 'red',    # Cara superior
    6: 'orange'      # Cara inferior
}

# Definir las matrices que representan las caras del cubo de Rubik
cara_frontal = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
cara_trasera = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
cara_izquierda = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
cara_derecha = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
cara_superior = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
cara_inferior = [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
cara_invisible = np.zeros((3, 3))

rubiks_cube = np.array([cara_superior, cara_izquierda, cara_frontal, cara_inferior, cara_derecha, cara_trasera]) 
rubiks_cube = r_up(rubiks_cube)
rubiks_cube = l_up(rubiks_cube)
rubiks_cube = u_left(rubiks_cube)
rubiks_cube = d_right(rubiks_cube)
rubiks_cube = r_up(rubiks_cube)
rubiks_cube = f_left(rubiks_cube)
rubiks_cube = b_left(rubiks_cube)

caras = [
    [cara_invisible, rubiks_cube[0], cara_invisible, cara_invisible],
    [rubiks_cube[1], rubiks_cube[2], rubiks_cube[4], rubiks_cube[5]],
    [cara_invisible, rubiks_cube[3], cara_invisible, cara_invisible]
]

# Crear un mapeo de colores categóricos
cmap = ListedColormap([colores[i] for i in range(1, 7)])

# Crear una figura para mostrar las caras del cubo de Rubik
fig, axs = plt.subplots(3, 4)

# Visualizar cada cara
for i, fila in enumerate(caras):
    for j, cara in enumerate(fila):
        ax = axs[i, j]

        if np.array_equal(cara, np.zeros((3, 3))):
            ax.axis('off')  # Deshabilitar la visualización para las caras invisibles
        else:
            ax.imshow(cara, cmap=cmap, vmin=0.5, vmax=6.5)  # Ajustar los límites para que coincidan con los valores de los colores
            ax.tick_params(axis='both', which='both', length=0)  # Eliminar las marcas de los ejes
            ax.set_xticks([])  # Eliminar marcas de los ejes x
            ax.set_yticks([])  # Eliminar marcas de los ejes y
            ax.grid(True, which='both', color='black', linestyle='-', linewidth=2)  # Mostrar cuadrícula
            ax.set_xticks(np.arange(-0.5, 3, 1), minor=True)  # Agregar marcas menores en el eje x
            ax.set_yticks(np.arange(-0.5, 3, 1), minor=True)  # Agregar marcas menores en el eje y

plt.tight_layout()
plt.show()
