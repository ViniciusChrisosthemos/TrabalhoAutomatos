import copy
class State:

    def __init__(self, id):
        self.id = id
        self.transition = {}
        self.is_final = False

    def do_transition(self, symbol):
        if symbol in self.transition:
            return self.transition[symbol]
        
        return None

    def __repr__(self):
        return str(self.__dict__)