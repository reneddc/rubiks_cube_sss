import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from Cube_Class import Cube
from Validations import Validations
import random
from Actions import Actions

class RubiksCube:
    def __init__(self):
        self.validations = Validations()
        self.terminal_state = []
    
    def get_initial_state(self, media):#Return a Cube()
        initial_state = []
        if media == 0:
            initial_state = Cube(self.charge_values_from_file()) #charge the values from file
        else:
            initial_state = Cube(self.charge_values_from_mixer()) #charge the values from a mixer
        return initial_state
    
    
    def charge_values_from_file(self): #Get the matrix from the file
        new_cube = []
        face = []
        with open("initial_state.txt", 'r') as archivo:
            lines = archivo.readlines()
            for line in range(len(lines)):
                if lines[line] != '\n':
                    row = []
                    row = [int(value) for value in lines[line] if value != '\n']
                    face.append(row)
                    np_face = np.array(face)
                    end_matrix = False
                else:
                    end_matrix = True
                if end_matrix or line == len(lines)-1:
                    new_cube.append(np_face)
                    face = []
        np_new_cube = np.array(new_cube)
        validation_txt = self.validate_file_values(np_new_cube)
        if validation_txt != "Correcto":
            np_new_cube = []
        print(validation_txt)   
        print() 
        return np_new_cube
    
    def validate_file_values(self, faces_to_validate):  
        return self.validations.get_result_validations(faces_to_validate) 
    
    def charge_values_from_mixer(self):
        movements = Actions()
        list_movs = movements.set_actions()
        self.get_goal_state()
        cube = self.terminal_state.get_matrix()
        for i in range(20):#20 movements random
            next_mov = random.randint(0,11)
            cube = movements.do_action(list_movs[next_mov][0], cube)
        return cube
        
        
    def get_goal_state(self): #Return a Cube()
        u_face = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])        #Red face
        l_face = np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]])        #Green face
        f_face = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])        #Yellow face
        d_face = np.array([[6, 6, 6], [6, 6, 6], [6, 6, 6]])        #Orange face
        r_face = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])        #Blue face
        b_face = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])        #White face
        self.terminal_state = Cube(np.array([u_face, l_face, f_face, d_face, r_face, b_face]))
        return self.terminal_state
        
    def set_new_state(self, new_cube):
        self.cube.set_new_faces(new_cube)
        self.print_cube(self.get_cube())

    def use_action(self, action):
        new_cube = self.actions.do_action(action, self.get_cube())
        self.set_new_state(new_cube)
        
 
