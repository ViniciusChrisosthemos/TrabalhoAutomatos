class Automaton:

    def __init__(self, id, states, symbols, initial_state):
        self.id = id
        self.states = states
        self.symbols = symbols
        self.initial_state = initial_state

    def validateWord(self, word):
        states = [self.initial_state]

        try:
            for symbol in word:
                new_states = []
                for state in states:
                    new_states.extend(state.do_transition(symbol))
                states = new_states

            for state in states:
                if state.is_final:
                    return True

            return False
        except KeyError:
            return False

    def __repr__(self):
        copy = self.__dict__.copy()
        copy['initial_state'] = copy['initial_state'].id
        return str(copy)