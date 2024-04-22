import numpy as np

class Actions:
    def __init__(self, actions = []):
        self.actions = actions
        
    def set_actions(self):
        self.actions = ["r_up", "r_down", "l_up", "l_down", "u_left", "u_right", "d_left", "d_right", "f_left", "f_right", "b_left", "b_right"]
        
    def get_actions(self):
        return self.actions