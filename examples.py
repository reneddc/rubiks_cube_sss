import numpy as np
from Faces import Faces

u_face = np.array([[0,0,'u'], [1,1,'u'], [2,2,'u']]) #Red face
l_face = np.array([[3,3,'l'], [4,4,'l'], [5,5,'l']])#Green face
f_face = np.array([[6,6,'f'], [7,7,'f'], [8,8,'f']])  #Yellow face
d_face = np.array([[15,15,'d'], [16,16,'d'], [17,17,'d']])  #Orange face
r_face = np.array([[9,9,'r'], [10,10,'r'], [11,11,'r']])  #Blue face
b_face = np.array([['b',12,12], ['b',13,13], ['b',14,14]])  #White face

rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 

r_actions = [0,2,3,5] #u,f,d,b -> up[2,3,5,0]
l_actions = [0,2,3,5]

u_actions = [0,1,4,5]
d_actions = [0,1,4,5]

f_actions = [0,1,3,5]
b_actions = [0,1,3,5]

def turn_face(face):
    face_reverse = face[::-1]
    new_face = np.transpose(face_reverse).tolist()
    return new_face

def turn_face_prime(face):
    new_face = np.transpose(face).tolist()
    new_face = new_face[::-1]
    return new_face

def r_up(rubiks_cube):
    rubiks_cube[5] = rubiks_cube[5][::-1,::-1] #back_face
    new_cube = rubiks_cube.copy()
    new_cube[4] = turn_face(new_cube[4]) # rotando la cara
    rotation_list = np.roll(r_actions,shift = -1) #setea como debe ser el orden de cambio
    for i in range(4):
        new_cube[r_actions[i]][:, -1] = rubiks_cube[rotation_list[i]][:, -1]
    new_cube[5] = new_cube[5][::-1,::-1] #back_face
    return new_cube
    


# result = turn_face(rubiks_cube[0])
# print(result)
# result = turn_face_prime(rubiks_cube[0])
# print(result)

faces = Faces()
print(faces)
print(r_up(rubiks_cube))