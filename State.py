from Cube_Class import Cube

class State:
    def __init__(self, cube): # Here cube is a class Cube(matrix) from Cube_Class.py
        self.cube = cube
        self.value = self.cube.get_hash_value()
        self.visited = False
        self.actions = [] #A list of actions [(State(),weight), (State(),weight)]
        self.parent = None
        self.cost = None
        
    def get_hash_value(self):
        return self.value
    
    def add_action(self, other_value):#other_value is a tuple
        if other_value not in self.actions:
            self.actions.append(other_value)

    def get_actions(self):
        return self.cube.get_movements()
        
    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def set_parent(self, parent):
        self.parent = parent
        
    def was_reached(self):
        return self.cost is not None or self.parent is not None
    
    def set_cost(self, cost): #the cost from 
        self.cost = cost

    def __lt__(self, other):
        return self.value <= other.value

    def __str__(self):
        return f"{self.value}, visited:{self.visited} -> {self.actions}"