import numpy as np
        
class Cube:
    def __init__(self):
        self.terminal_state = []
        self.faces = []
        
    def set_ordered_state(self): # Set the goal_state
        u_face = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])        #Red face
        l_face = np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]])        #Green face
        f_face = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])        #Yellow face
        d_face = np.array([[6, 6, 6], [6, 6, 6], [6, 6, 6]])  #Orange face
        r_face = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])    #Blue face
        b_face = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])  #White face
        self.faces = np.array([u_face, l_face, f_face, d_face, r_face, b_face])
        self.terminal_state = self.faces.copy()
        
    def initial_state(self, media):#Define the initial state
        new_faces = []
        if media == 0:
            new_faces = self.charge_values_from_file() #charge the values from file
        else:
            new_faces = self.charge_values_from_mixer() #charge the values from a mixer
        self.set_new_faces(new_faces)
        
    def charge_values_from_file():
        
        
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
