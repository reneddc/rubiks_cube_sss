import numpy as np
from Faces import Faces
from Actions2 import Actions

class RubiksCube:
    def __init__(self):
        self.faces = Faces()
        self.actions = Actions()
        
    def set_rubik(self):
        self.faces.set_initial_face()
        self.actions.set_actions()
        self.faces.print_faces()
        
    def set_new_state(self, action):
        self.faces = self.use_action(action)
        self.faces.print_faces()

    def use_action(self, action):
        switch = {1: self.r_up(),
                  2: self.r_down()}
        funcion = switch.get(opcion, default_case)
        return new_state
    
    def print_faces():
        return 0


rubik = RubiksCube()
rubik.set_rubik()
