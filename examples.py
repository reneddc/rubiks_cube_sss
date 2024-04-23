import numpy as np

u_face = np.array([[0,0,'u'], [1,1,'u'], [2,2,'u']]) #Red face
l_face = np.array([[3,3,'l'], [4,4,'l'], [5,5,'l']])#Green face
f_face = np.array([[6,6,'f'], [7,7,'f'], [8,8,'f']])  #Yellow face
d_face = np.array([[9,9,'d'], [10,10,'d'], [11,11,'d']])  #Orange face 
r_face = np.array([[12,12,'r'], [13,13,'r'], [14,14,'r']])  #Blue face
b_face = np.array([['b',15,15], ['b',16,16], ['b',17,17]])   #White face

rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 

r_actions = [0,2,3,5] #u,f,d,b -> up[2,3,5,0]  down [5,0,2,3] prime
l_actions = [0,2,3,5] #u,f,d,b -> up[2,3,5,0]  prime down [5,0,2,3] 

u_actions = [1,2,4,5] # left    [2,4,5,1]           right     [5,1,2,4] prime 
d_actions = [1,2,4,5] # left    [2,4,5,1]  prime    right     [5,1,2,4]         
  
b_actions = [0,4,3,1] #left     [4,3,1,0]           right     [1,0,4,3] prime
f_actions = [0,4,3,1] #left     [4,3,1,0] prime     right     [1,0,4,3]



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

def l_action(rubiks_cube, rotate_up):
    rubiks_cube[5] = rubiks_cube[5][::-1,::-1]
    new_cube = rubiks_cube.copy()
    rotate_direction = True if rotate_up else False
    new_cube[1] = turn_face(new_cube[1], rotate_direction)
    rotation_list = np.roll(l_actions, shift=-1 if rotate_up else 1)
    for i in range(4):
        print(rubiks_cube[rotation_list[i]][:, 0])
        new_cube[l_actions[i]][:, 0] = rubiks_cube[rotation_list[i]][:, 0]
    new_cube[5] = new_cube[5][::-1,::-1]
    return new_cube

def u_action(rubiks_cube, rotate_up):
    new_cube = rubiks_cube.copy()
    rotate_direction = False if rotate_up else True
    new_cube[0] = turn_face(new_cube[0], rotate_direction)
    rotation_list = np.roll(u_actions, shift=-1 if rotate_up else 1)
    for i in range(4):
        new_cube[u_actions[i]][0] = rubiks_cube[rotation_list[i]][0]
    return new_cube

def d_action(rubiks_cube, rotate_up):
    new_cube = rubiks_cube.copy()
    rotate_direction = True if rotate_up else False
    new_cube[3] = turn_face(new_cube[3], rotate_direction)
    rotation_list = np.roll(u_actions, shift=-1 if rotate_up else 1)
    for i in range(4):
        new_cube[u_actions[i]][2] = rubiks_cube[rotation_list[i]][2]
    return new_cube

def f_action(rubiks_cube, rotate_up):
    rubiks_cube[1] = rubiks_cube[1][::-1,::-1]
    rubiks_cube[0] = turn_face(rubiks_cube[0], False)
    rubiks_cube[3] = turn_face(rubiks_cube[3], True)
    print(rubiks_cube[3])
    new_cube = rubiks_cube.copy()
    rotate_direction = True if rotate_up else False
    new_cube[2] = turn_face(new_cube[2], rotate_direction)
    rotation_list = np.roll(f_actions, shift=-1 if rotate_up else 1)
    for i in range(4):
        new_cube[f_actions[i]][:, 0] = rubiks_cube[rotation_list[i]][:, 0]
    new_cube[1] = new_cube[1][::-1,::-1]
    new_cube[0] = turn_face(new_cube[0], True)
    new_cube[3] = turn_face(new_cube[3], False)
    return new_cube


def b_action(rubiks_cube, rotate_up):
    rubiks_cube[1] = rubiks_cube[1][::-1,::-1]
    rubiks_cube[0] = turn_face(rubiks_cube[0], False)
    rubiks_cube[3] = turn_face(rubiks_cube[3], True)
    print(rubiks_cube[3])
    new_cube = rubiks_cube.copy()
    rotate_direction = False if rotate_up else True
    new_cube[5] = turn_face(new_cube[5], rotate_direction)
    rotation_list = np.roll(f_actions, shift=-1 if rotate_up else 1)
    for i in range(4):
        new_cube[f_actions[i]][:, -1]  = rubiks_cube[rotation_list[i]][:, -1] 
    new_cube[1] = new_cube[1][::-1,::-1]
    new_cube[0] = turn_face(new_cube[0], True)
    new_cube[3] = turn_face(new_cube[3], False)
    return new_cube

def r_up(rubiks_cube):
    return r_action(rubiks_cube, True)

def r_down(rubiks_cube):
    return r_action(rubiks_cube, False)

def l_up(rubiks_cube):
    return l_action(rubiks_cube, True)

def l_down(rubiks_cube):
    return l_action(rubiks_cube, False)

def u_left(rubiks_cube):
    return u_action(rubiks_cube, True)

def u_right(rubiks_cube):
    return u_action(rubiks_cube, False)

def d_left(rubiks_cube):
    return d_action(rubiks_cube, True)

def d_right(rubiks_cube):
    return d_action(rubiks_cube, False)

def f_left(rubiks_cube):
    return f_action(rubiks_cube, True)

def f_right(rubiks_cube):
    return f_action(rubiks_cube, False)

def b_left(rubiks_cube):
    return b_action(rubiks_cube, True)

def b_right(rubiks_cube):
    return b_action(rubiks_cube, False)
    





# print("R_UP------------------")
# rubiks_cube = r_up(rubiks_cube)
# print(rubiks_cube)

# print()
# print("R_DOWN------------------")
# print(r_down(rubiks_cube))

# print()
# print("L_UP------------------")
# print(l_up(rubiks_cube))

# rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 
# print()
# print("L_DOWN------------------")
# print(l_down(rubiks_cube))


# print("U_LEFT------------------")
# print(u_left(rubiks_cube))

# rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 
# print()
# print("U_RIGHT------------------")
# print(u_right(rubiks_cube))

# print("D_LEFT------------------")
# print(d_left(rubiks_cube))

# rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 
# print()
# print("D_RIGHT------------------")
# print(d_right(rubiks_cube))

print("F_LEFT------------------")
print(b_left(rubiks_cube))

rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 
print()
print("F_RIGHT------------------")
print(b_right(rubiks_cube))