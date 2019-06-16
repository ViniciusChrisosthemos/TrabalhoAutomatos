import copy
class State:

    def __init__(self, id):
        self.id = id
        self.transitions = {}
        self.is_final = False

    def do_transition(self, symbol):
        if symbol in self.transitions:
            return self.transitions[symbol]
        
        return None

    def __repr__(self):
        copy = self.__dict__.copy()
        transitions = []
        for symbol in copy["transitions"]:
            transitions.extend([(symbol, state) for state in copy['transitions'][symbol]])
        copy["transitions"] = transitions

        return str(copy)