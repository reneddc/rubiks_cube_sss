import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from Faces import Cube
from Actions import Actions

class RubiksCube:
    def __init__(self):
        self.cube = Cube()
        self.actions = Actions()
        
    def set_rubik(self):
        self.cube.set_ordered_state()
        self.actions.set_actions()
    
    def set_initial_state(self, media):
        self.cube.set_initial_state(media)
        
    def get_cube(self):
        return self.cube.get_faces()
        
    def set_new_state(self, new_cube):
        self.cube.set_new_faces(new_cube)
        self.print_cube(self.get_cube())

    def use_action(self, action):
        new_cube = self.actions.do_action(action, self.get_cube())
        self.set_new_state(new_cube)
        
    def is_terminal(self):
        return self.cube.is_terminal()
        
    def print_cube(self, faces):
        colores = {
            1: 'yellow',       # Cara frontal
            2: 'white',    # Cara trasera
            3: 'green',     # Cara izquierda
            4: 'blue',      # Cara derecha
            5: 'red',    # Cara superior
            6: 'orange'      # Cara inferior
        }
        cara_invisible = np.zeros((3, 3))
        caras = [[cara_invisible, faces[0], cara_invisible, cara_invisible],
                [faces[1], faces[2], faces[4], faces[5]],
                [cara_invisible, faces[3], cara_invisible, cara_invisible]]
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


rubik = RubiksCube()
rubik.set_rubik()
print(rubik.is_terminal())
rubik.use_action("f_right")
print(rubik.is_terminal())
rubik.use_action("f_left")
print(rubik.is_terminal())

