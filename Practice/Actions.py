# All the moves are centered by the yellow center as front view, 
# the red face as upper view and the green face as a left lateral view
import numpy as np

u_face = np.array([[0,0,'u'], [1,1,'u'], [2,2,'u']]) #Red face
l_face = np.array([[3,3,'l'], [4,4,'l'], [5,5,'l']])#Green face
f_face = np.array([[6,6,'f'], [7,7,'f'], [8,8,'f']])  #Yellow face
d_face = np.array([[15,15,'d'], [16,16,'d'], [17,17,'d']])  #Orange face
r_face = np.array([[9,9,'r'], [10,10,'r'], [11,11,'r']])  #Blue face
b_face = np.array([['b',12,12], ['b',13,13], ['b',14,14]])  #White face


r_actions = [0,2,3,5] #u,f,d,b
l_actions = [0,2,3,5]

u_actions = [0,1,4,5]
d_actions = [0,1,4,5]

f_actions = [0,1,3,5]
b_actions = [0,1,3,5]

def r_action(rubiks_cube, side):
    face = rubiks_cube[4]
    rubiks_cube[5] = rubiks_cube[5][:, ::-1] #Sorting the columns to work easier
    if side == "Up":
        new_face = turn_face(face)
        values_to_change = [rubiks_cube[matriz][:, -1] for matriz in r_actions]
        print("matriz que cambia")
        print(values_to_change)
        movement = np.roll(values_to_change,1)
        
        print(movement)
        print(r_actions)
        for i in range(4):
            print(i)
            rubiks_cube[r_actions[i]][:, -1] = movement[i]#down   
    else:
        new_face = turn_face_prime(face)
        # for i in range(3):
        #     rubiks_cube[r_actions[i]][:, -1] = values_to_change[(3-i) % 4]#down  
    rubiks_cube[4] = new_face
    rubiks_cube[5] = rubiks_cube[5][:, ::-1]
    return rubiks_cube
      
#1,2,3,0

def turn_face(face):
    face_reverse = face[::-1]
    new_face = np.transpose(face_reverse).tolist()
    return new_face

def turn_face_prime(face):
    new_face = np.transpose(face).tolist()
    new_face = new_face[::-1]
    return new_face

rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) # 0,1,2,3,4,5

face_r_up = turn_face(r_face)
face_r_down = turn_face_prime(r_face)


print("R Arriba")
print(face_r_up)
print("R Abajo")
print(face_r_down)


print(r_action(rubiks_cube, "Up"))

            
    