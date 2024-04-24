from State import State
from Cube_Class import Cube

class StateSpace():
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        self.states[state.value] = state #A dictionary of states {hash_value1: (State(),weight), hash_value2: (State(),weight)}
        actions = self.states[state.value].get_actions()
        for action in actions:
            list_tuple = list(action)
            list_tuple[0] = State(Cube(action[0]))
            new_action_tuple = tuple(list_tuple)
            self.add_action(state.value, new_action_tuple)#the states here aren't in space yet
        
    def add_action(self, value1, value2):#value1 is the hash and value 2 is the tuple
        self.states[value1].add_action(value2)
        
    def get_state(self, value):
        if type(value) == tuple: #is tuple
            if value[0].value not in self.states:
                self.add_state(value[0])
                value[0].set_cost(1)
            return self.states[value[0].value]# value[0] is a State() and .value is the hash
        return self.states[value]

    def add_edge(self, value1, value2): 
        self.states[value1].add_action(value2)

    def add_weighted_edge(self, value1, value2, weight): 
        self.states[value1].add_action((value2, weight)) #Value1 = state.hash_value, Value2 = state.hash_value

    def reset_visits(self):
        for state in self.states.values():
            state.mark_unvisited()