from queue import PriorityQueue
from Frontier import *

class Searcher:
    def __init__(self, space):
        self.space = space

    # def breadth_first(self, initial_value, end_value):
    #     return self.search(initial_value, end_value, Queue())

    # def depth_first(self, initial_value, end_value):
    #     return self.search(initial_value, end_value, Stack())
    
    # def search(self, initial_value, end_value, frontier):
    #     initial_state = self.space.get_state(initial_value)
    #     frontier.push(initial_state)

    #     while frontier:
    #         current_state = frontier.pop()
    #         current_state.mark_visited()

    #         if current_state.value == end_value:
    #             return self.build_solution_path(current_state)

    #         for action in current_state.actions:
    #             next_state = self.space.get_state(action)
    #             if not next_state.visited and not frontier.has(next_state):
    #                 next_state.set_parent(current_state)
    #                 frontier.push(next_state)
    #     return []
    
    def uniform_cost(self, initial_value, end_value):
        return self.weighted_search(initial_value, end_value, PriorityQueue())

    def weighted_search(self, intial_value, goal_value, frontier):
        initial_state = self.space.get_state(intial_value)
        initial_state.set_cost(0)
        frontier.put((initial_state, 0))

        while not frontier.empty():
            current_state, current_cost = frontier.get()
            current_state.mark_visited()
            if self.debug: print(current_state.value, current_cost)

            if current_state.value == goal_value:
                if self.debug: print("Goal found")
                return self.build_solution_path(current_state), current_cost

            for action in current_state.actions:
                next_state = self.space.get_state(action)
                action_cost = current_cost + action[1]

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