from queue import PriorityQueue
from Frontier import *

class Searcher:
    def __init__(self, space, debug=False):
        self.space = space
        self.debug = debug
    
    def uniform_cost(self, initial_value, end_value):
        return self.weighted_search(initial_value, end_value, PriorityQueue())

    def weighted_search(self, intial_value, goal_value, frontier): #here we are working with the hash of the state of the cube
        initial_state = self.space.get_state(intial_value)#State()
        initial_state.set_cost(0)
        frontier.put((initial_state, 0)) #frontier has State() and its respective weight

        while not frontier.empty():
            current_state, current_cost = frontier.get() #current state is a State()
            current_state.mark_visited()
            if self.debug: print(current_state.value, current_cost)

            if current_state.value == goal_value: #is terminal state?
                if self.debug: print("Goal found")
                return self.build_solution_path(current_state), current_cost #list of the actions

            for action in current_state.actions:
                next_state = self.space.get_state(action) #action is a tuple of (State(), weight)
                action_cost = current_cost + action[1] #action[1] is weight

                if not next_state.was_reached() or action_cost < next_state.cost:
                    next_state.set_parent(current_state)
                    next_state.set_cost(action_cost)

                    if self.debug:print("Expanding:", next_state.value, action_cost)
                    frontier.put((next_state, action_cost))
        return []

    def build_solution_path(self, state):
        path = []
        while state:
            path.append(state.value)
            state = state.parent
        return list(reversed(path))