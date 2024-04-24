from State import State
from SpaceStates import StateSpace
from Searcher import Searcher
from RubiksCube import RubiksCube
from CubeClass import Cube

if __name__ == "__main__":
    
    
    
    state_values = space_dict.keys()

    space  = StateSpace()

    for value in state_values:
        space.add_state(State(value))

    for state, actions in space_dict.items():
        for action in actions:
            if type(action) == tuple:
                space.add_weighted_edge(state, action[0], action[1])
            else:
                space.add_edge(state, action)

    rubik = RubiksCube()
    rubik.set_rubik()
    initial_value = rubik.set_initial_state(0)
    end_value = rubik.get_terminal_state()

    searcher = Searcher(space)

    print("Buscando en costo uniforme")
    print(searcher.uniform_cost(initial_value, end_value))