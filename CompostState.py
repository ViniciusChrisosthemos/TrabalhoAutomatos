from State import State

class CompostState:

    def __init__(self, states):
        self.id = ""
        self.is_final = False
        states = sorted(states)
        for state in states:
            self.id += state
        self.transitions = {}

    def get_state(self):
        return State(self.id, self.is_final, self.transitions)

    def __repr__(self):
        return str(self.__dict__)