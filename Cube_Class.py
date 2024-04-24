import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import json
from Faces_Validations import Validations
        
class Cube:
    def __init__(self, matrix):
        self.matrix = matrix.copy()
        self.hash_value
        
    def get_hash_value(self):
        self.get_hash_value = json.dumps(self.matrix, sort_keys=True)
        return self.get_hash_value()
    
    def print_cube(self):
        colores = {
            1: 'yellow',        # Cara frontal
            2: 'white',         # Cara trasera
            3: 'green',         # Cara izquierda
            4: 'blue',          # Cara derecha
            5: 'red',           # Cara superior
            6: 'orange'         # Cara inferior
        }
        cara_invisible = np.zeros((3, 3))
        caras = [[cara_invisible, self.matrix[0], cara_invisible, cara_invisible],
                [self.matrix[1], self.matrix[2], self.matrix[4], self.matrix[5]],
                [cara_invisible, self.matrix[3], cara_invisible, cara_invisible]]
        cmap = ListedColormap([colores[i] for i in range(1, 7)])
        fig, axs = plt.subplots(3, 4)
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