import copy
class State:

    def __init__(self, id, is_final=False, transitions={}):
        self.id = id
        self.transitions = transitions
        self.is_final = is_final

    def do_transition(self, symbol):
        states = []
        try:
            states = self.transitions[symbol]
            return states
        except KeyError:
            return []

    def __repr__(self):
        copy = self.__dict__.copy()
        return str(copy)