from State import State
from RubiksCube import RubiksCube

class StateSpace():
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        self.states[state.value] = state #A dictionary of states {hash_value1: (State(),weight), hash_value2: (State(),weight)}

    def get_state(self, value):
        if type(value) == tuple:
            return self.states[value[0]]
        return self.states[value]

    def add_edge(self, value1, value2): 
        self.states[value1].add_action(value2)

    def add_weighted_edge(self, value1, value2, weight): 
        self.states[value1].add_action((value2, weight)) #Value1 = state.hash_value, Value2 = state.hash_value

    def reset_visits(self):
        for state in self.states.values():
            state.mark_unvisited()