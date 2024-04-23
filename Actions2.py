import numpy as np

class Actions:
    def __init__(self):
        #impares son antihorario, primos (')
        self.actions = []
        self.faces_dict = {0:4, 1:1, 2:0, 3:3, 4:5, 5:2 }
        self.r_l_actions = [0,2,3,5]
        self.u_d_actions = [1,2,4,5]
        self.b_f_actions = [0,4,3,1]
    
    #Here the name of the action and the side tu turn are setted        
    def set_actions(self): 
        #The actions are order with care to be aeasily to know which follows the clock's movement
        list_actions = ["r_up", "r_down", "l_down", "l_up", "u_left", "u_right", "d_right", "d_left", "b_left", "b_right", "f_right", "f_left"]
        for action in list_actions:
            side = False
            if "left" in action or "up" in action:
                side = True
            self.actions.append((action,side))
        return self.actions
    
    def get_actions(self):
        return self.actions
    
    #Here the user provides the name of the action and returns the index and the side tu turn
    def get_index_action(self, action):
        action_name = [action[0] for action in self.actions]
        index = action_name.index(action)
        return (index, self.actions[index][1])
    
    #This set the direction of the rotation of the face
    def set_rotate_direction(self, index):
        return False if index%2 == 0 else True
    
    #Rotate the face
    def turn_face(self, face, prime):
        if prime:
            new_face = np.rot90(face, ).tolist()
        else:
            new_face = np.rot90(face, 3).tolist()
        return new_face
    
    #Transpose the white or another face
    def transpose_face(self, face):
        face_transposed= face[::-1,::-1]
        return face_transposed
    
    #by the index of the action, this get the face that will rotate
    def get_face_to_turn(self, index):
        index_action = index//2
        return self.faces_dict[index_action]
    
    #changes the values between the faces involved
    def change_values(self, actions, original_cube, new_cube, rotation_list, action):
        if action == 4 or action == 5:
            for i in range(4):
                new_cube[actions[i]][:, -1] = original_cube[rotation_list[i]][:, -1]
        if action == 1 or action == 2:
            for i in range(4): 
                new_cube[actions[i]][:, 0] = original_cube[rotation_list[i]][:, 0]
        if action == 0:
            for i in range(4):
                new_cube[actions[i]][0] = original_cube[rotation_list[i]][0]
        if action == 3:
            for i in range(4):
                new_cube[actions[i]][2] = original_cube[rotation_list[i]][2]
        return new_cube   
    
    def do_r_l_action(self, action, rubiks_cube):
        print("Acción: " + action)
        index, side = self.get_index_action(action)
        rotate_direction = self.set_rotate_direction(index)
        rubiks_cube[5] = self.transpose_face(rubiks_cube[5])
        face_to_turn = self.get_face_to_turn(index)
        new_cube = rubiks_cube.copy()
        new_cube[face_to_turn] = self.turn_face(new_cube[face_to_turn], rotate_direction)
        rotation_list = np.roll(self.r_l_actions, shift=-1 if side else 1)
        new_cube = self.change_values(self.r_l_actions, rubiks_cube, new_cube, rotation_list, face_to_turn)
        new_cube[5] = new_cube[5][::-1,::-1]
        return new_cube
    
    def do_u_d_actions(self, action, rubiks_cube):
        print("Acción: " + action)
        index, side = self.get_index_action(action)
        rotate_direction = self.set_rotate_direction(index)
        face_to_turn = self.get_face_to_turn(index)
        new_cube = rubiks_cube.copy()
        new_cube[face_to_turn] = self.turn_face(new_cube[face_to_turn], rotate_direction)
        rotation_list = np.roll(self.u_d_actions, shift=-1 if side else 1)
        new_cube = self.change_values(self.u_d_actions, rubiks_cube, new_cube, rotation_list, face_to_turn)
        return new_cube
    
    def do_b_f_actions(self, action, rubiks_cube):
        rubiks_cube[1] = self.transpose_face(rubiks_cube[1])
        rubiks_cube[0] = self.turn_face(rubiks_cube[0], False)
        rubiks_cube[3] = self.turn_face(rubiks_cube[3], True)
        index, side = self.get_index_action(action)
        face_to_turn = self.get_face_to_turn(index)
        print(face_to_turn, index)
        rotate_direction = self.set_rotate_direction(index)
        new_cube = rubiks_cube.copy()
        new_cube[face_to_turn] = self.turn_face(new_cube[face_to_turn], rotate_direction)
        rotation_list = np.roll(self.b_f_actions, shift=-1 if side else 1)
        new_cube = self.change_values(self.b_f_actions, rubiks_cube, new_cube, rotation_list, face_to_turn)
        new_cube[1] = self.transpose_face(new_cube[1])
        new_cube[0] = self.turn_face(new_cube[0], True)
        new_cube[3] = self.turn_face(new_cube[3], False)
        return new_cube
    
    #     rubiks_cube[1] = rubiks_cube[1][::-1,::-1]
    # rubiks_cube[0] = turn_face(rubiks_cube[0], False)
    # rubiks_cube[3] = turn_face(rubiks_cube[3], True)
    # new_cube = rubiks_cube.copy()
    # rotate_direction = True if rotate_up else False
    # new_cube[2] = turn_face(new_cube[2], rotate_direction)
    # rotation_list = np.roll(f_actions, shift=-1 if rotate_up else 1)
    # for i in range(4):
    #     new_cube[f_actions[i]][:, 0] = rubiks_cube[rotation_list[i]][:, 0]
    # new_cube[1] = new_cube[1][::-1,::-1]
    # new_cube[0] = turn_face(new_cube[0], True)
    # new_cube[3] = turn_face(new_cube[3], False)
 

u_face = np.array([[0,0,'u'], [1,1,'u'], [2,2,'u']]) #Red face
l_face = np.array([[3,3,'l'], [4,4,'l'], [5,5,'l']])#Green face
f_face = np.array([[6,6,'f'], [7,7,'f'], [8,8,'f']])  #Yellow face
d_face = np.array([[9,9,'d'], [10,10,'d'], [11,11,'d']])  #Orange face 
r_face = np.array([[12,12,'r'], [13,13,'r'], [14,14,'r']])  #Blue face
b_face = np.array([['b',15,15], ['b',16,16], ['b',17,17]])   #White face

rubiks_cube = np.array([u_face, l_face, f_face, d_face, r_face, b_face]) 

action = Actions() 
action.set_actions()

rubiks_cube = action.do_b_f_actions("b_right", rubiks_cube)
print(rubiks_cube) 
    
 