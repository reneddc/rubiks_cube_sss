import numpy as np
from Faces_Validations import Validations
        
class Cube:
    def __init__(self):
        self.terminal_state = []
        self.faces = []
        self.validations = Validations()
        
    def get_goal_state(self):
        u_face = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])        #Red face
        l_face = np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]])        #Green face
        f_face = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])        #Yellow face
        d_face = np.array([[6, 6, 6], [6, 6, 6], [6, 6, 6]])        #Orange face
        r_face = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])        #Blue face
        b_face = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])        #White face
        self.terminal_state = np.array([u_face, l_face, f_face, d_face, r_face, b_face])
        return self.terminal_state
        
    def get_initial_state(self, media):#Define the initial state
        new_faces = []
        if media == 0:
            new_faces = self.charge_values_from_file() #charge the values from file
        else:
            new_faces = self.charge_values_from_mixer() #charge the values from a mixer
        self.set_new_faces(new_faces)
        
    def charge_values_from_file(self):
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
            
    def set_new_faces(self, new_faces):#define new state
        self.faces = new_faces.copy()    
    
    def get_faces(self):#Return the current state
        return self.faces 
    
    def is_terminal(self):#return if the current state is the correct
        terminal = np.array_equal(self.terminal_state,self.faces)
        return terminal
    
    def transpose_face(self, face):#transpose a face
        face_transposed= face[::-1,::-1]
        return face_transposed
    
    def get_terminal_cube(self):
        return self.terminal_state