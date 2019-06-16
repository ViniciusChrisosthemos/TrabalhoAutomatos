class Automaton:

    def __init__(self, states, symbols, initial_state):
        self.states = states
        self.symbols = symbols
        self.initial_state = initial_state

    def validateWord(self, word):
        state = self.initial_state
        try:
            for symbol in word:
                state = state.do_transition(symbol)
            
            return state.is_final
        except RuntimeError:
            return False
