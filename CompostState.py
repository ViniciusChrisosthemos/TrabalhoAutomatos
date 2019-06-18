from State import State

class CompostState:

    def __init__(self, states):
        self.id = ""
        self.is_final = False
        print("\n", states, "\n")
        for state in states:
            self.id += state.id
            if state.is_final:
                self.is_final = True

        self.states = set(states)
        self.transitions = {}

    def get_transitions(self, symbol):
        states = []
        for state in self.states:
            if symbol in state.transitions:
                states.extend(state.transitions[symbol])

        return states

    def get_state(self):
        state = State(self.id)
        state.transitions = self.transitions
        state.is_final = self.is_final

        return state

    def __repr__(self):
        return str(self.__dict__)