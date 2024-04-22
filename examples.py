import numpy as np

u_face = np.array([[0,0,'u'], [1,1,'u'], [2,2,'u']]) #Red face
l_face = np.array([[3,3,'l'], [4,4,'l'], [5,5,'l']])#Green face
f_face = np.array([[6,6,'f'], [7,7,'f'], [8,8,'f']])  #Yellow face
d_face = np.array([[15,15,'d'], [16,16,'d'], [17,17,'d']])  #Orange face
r_face = np.array([[9,9,'r'], [10,10,'r'], [11,11,'r']])  #Blue face
b_face = np.array([['b',12,12], ['b',13,13], ['b',14,14]])  #White face

rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 

r_actions = [0,2,3,5] #u,f,d,b -> up[2,3,5,0] down [5,0,2,3]
l_actions = [0,2,3,5]

u_actions = [0,1,4,5]
d_actions = [0,1,4,5]

f_actions = [0,1,3,5]
b_actions = [0,1,3,5]

def turn_face(face, prime):
    if prime:
        new_face = np.rot90(face, ).tolist()  # Rotar 180 grados
    else:
        new_face = np.rot90(face, 3).tolist()  # Rotar 90 grados en sentido horario
    return new_face

def r_action(rubiks_cube, rotate_up):
    rubiks_cube[5] = rubiks_cube[5][::-1,::-1]
    new_cube = rubiks_cube.copy()
    rotate_direction = False if rotate_up else True
    new_cube[4] = turn_face(new_cube[4], rotate_direction)
    rotation_list = np.roll(r_actions, shift=-1 if rotate_up else 1)
    for i in range(4):
        new_cube[r_actions[i]][:, -1] = rubiks_cube[rotation_list[i]][:, -1]
    new_cube[5] = new_cube[5][::-1,::-1]
    return new_cube

def r_up(rubiks_cube):
    return r_action(rubiks_cube, True)

def r_down(rubiks_cube):
    return r_action(rubiks_cube, False)

print("R_UP------------------")
rubiks_cube = r_up(rubiks_cube)
print(rubiks_cube)

print()
print("R_DOWN------------------")
print(r_down(rubiks_cube))