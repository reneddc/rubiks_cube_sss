class Frontier:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def has(self, value):
        return value in self.values

    def is_empty(self):
        return len(self.values) == 0

class Queue(Frontier):
    def pop(self):
        return self.values.pop(0)

class Stack(Frontier):
    def pop(self):
        return self.values.pop()
