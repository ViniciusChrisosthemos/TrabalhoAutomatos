import copy
class State:

    def __init__(self, id):
        self.id = id
        self.transitions = {}
        self.is_final = False

    def do_transition(self, symbol):
        states = []
        try:
            states = self.transitions[symbol]
            return states
        except KeyError:
            return []

    def __repr__(self):
        copy = self.__dict__.copy()
        transitions = []
        for symbol in copy["transitions"]:
            transitions.extend([(symbol, state.id) for state in copy['transitions'][symbol]])
        copy["transitions"] = transitions

        return str(copy)