u_face = [[0,0,0], [0,0,0], [0,0,0]] #Red face
l_face = [[1,1,1], [1,1,1], [1,1,1]] #Green face
f_face = [[2,2,2], [2,2,2], [2,2,2]] #Yellow face
d_face = [[3,3,3], [3,3,3], [3,3,3]] #Orange face
r_face = [[4,4,4], [4,4,4], [4,4,4]] #Blue face
b_face = [[5,5,5], [5,5,5], [5,5,5]] #White face

def terminalState():
    rubiks_cube = [u_face, l_face, f_face, d_face, r_face, b_face]
    return rubiks_cube