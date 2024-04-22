from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define los colores de cada cara del cubo de Rubik
colores = {
    1: (1, 0, 0),    # Rojo
    2: (1, 0.5, 0),  # Naranja
    3: (0, 1, 0),    # Verde
    4: (0, 0, 1),    # Azul
    5: (1, 1, 0),    # Amarillo
    6: (1, 1, 1)     # Blanco
}

# Define las matrices que representan las caras del cubo de Rubik
cara_frontal = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
cara_trasera = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
cara_izquierda = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
cara_derecha = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
cara_superior = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
cara_inferior = [[6, 6, 6], [6, 6, 6], [6, 6, 6]]

# Define las posiciones de cada cara en el cubo de Rubik
caras_posiciones = {
    'frontal': cara_frontal,
    'trasera': cara_trasera,
    'izquierda': cara_izquierda,
    'derecha': cara_derecha,
    'superior': cara_superior,
    'inferior': cara_inferior
}

def draw_cube():
    glBegin(GL_QUADS)
    for cara, matriz_color in caras_posiciones.items():
        color = colores[matriz_color[1][1]]
        glColor3fv(color)
        for vertice in matriz_color:
            glVertex3fv(vertice)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 3, 1, 1)
    draw_cube()
    glutSwapBuffers()

# Inicializa OpenGL
glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b'Cubo de Rubik 3D')

# Configura la cámara
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (800/600), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)

# Configura la ventana
glClearColor(0.5, 0.5, 0.5, 1)
glEnable(GL_DEPTH_TEST)

# Ejecuta el bucle de dibujo
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
