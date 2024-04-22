import numpy as np
from Faces import Faces
from Actions2 import Actions

class Rubiks_Cube:
    def __init__(self, faces, actions):
        self.faces = faces
        self.actions = actions




def set_cube(rubik):
    
    return rubik



actions = Actions()
actions.set_actions()
faces = Faces()
faces.set_faces()
rubik = Rubiks_Cube(faces.get_faces(), actions.get_actions())
