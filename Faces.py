import numpy as np

class Faces:
    def __init__(self, cube = []):
        self.cube = cube
        
    def set_faces(self):
        u_face = np.array([[0,0,'u'], [1,1,'u'], [2,2,'u']])        #Red face
        l_face = np.array([[3,3,'l'], [4,4,'l'], [5,5,'l']])        #Green face
        f_face = np.array([[6,6,'f'], [7,7,'f'], [8,8,'f']])        #Yellow face
        d_face = np.array([[15,15,'d'], [16,16,'d'], [17,17,'d']])  #Orange face
        r_face = np.array([[9,9,'r'], [10,10,'r'], [11,11,'r']])    #Blue face
        b_face = np.array([[12,12,'b'], [13,13,'b'], [14,14,'b']])  #White face
        self.cube = [u_face, l_face, f_face, d_face, r_face, b_face]
        
    def get_faces(self):
        return self.cube
    
    def print_faces(self):
        for idx, array in enumerate(self.cube):
            print(f"Cara {idx}:")
            for row in array:
                print(" ".join(row))
            print()