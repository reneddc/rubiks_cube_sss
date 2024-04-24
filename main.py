from State import State
from SpaceStates import StateSpace
from Rubik_Cube import RubiksCube
from Searcher import Searcher

if __name__ == "__main__":
    debugging = False
    space  = StateSpace()
    rubik = RubiksCube()
    initial_state = State(rubik.get_initial_state(1)) #charging the values from the file
    goal_state = State(rubik.get_goal_state()) #Charging the terminal state
    # initial_state.print_cube()
    # goal_state.print_cube()
    
    space.add_state(initial_state)
    space.add_state(goal_state)
    
    searcher = Searcher(space, debug=debugging)
    
    print(initial_state.value)
    
    print("Buscar en costo uniforme")
    path, cost = searcher.uniform_cost(initial_state.value, goal_state.value)
    print(path, "costo:", cost)  
 
 
 