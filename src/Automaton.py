from src.CompostState import CompostState
import queue

class Automaton:

    def __init__(self, id, states, symbols, initial_state):
        self.id = id
        self.states = states
        self.symbols = symbols
        self.initial_state = initial_state

    def validate_word(self, word):
        states = [self.initial_state.id]

        try:
            for symbol in word:
                new_states = []
                for state in states:
                    new_states.extend(self.states[state].do_transition(symbol))
                states = new_states

            for state in states:
                if self.states[state].is_final:
                    return True

            return False
        except KeyError:
            return False

    def get_transitions(self, c_state, symbol):
        states = []

        for state in self.states:
            if self.states[state].id in c_state.states:
                if symbol in self.states[state].transitions:
                    states.extend(self.states[state].transitions[symbol])

        return list(set(states))

    def to_afd(self):
        mqueue = queue.Queue()
        new_states = {}
        mqueue.put(CompostState([self.initial_state.id]))

        while not mqueue.empty():
            c_state = mqueue.get()

            for symbol in self.symbols:
                transitions = self.get_transitions(c_state, symbol)
                if not transitions: 
                    continue

                temp_state = CompostState(transitions)
                c_state.transitions[symbol] = [temp_state.id]

                if temp_state.id not in new_states:
                    mqueue.put(temp_state)

            new_states[c_state.id] = c_state

        for state in self.states:
            for c_state in new_states:
                if self.states[state].is_final and self.states[state].id in new_states[c_state].id:
                    new_states[c_state].is_final = True
            
        states = {}
        for state in new_states:
            states[state] = new_states[state].get_state()

        return Automaton('AFD-'+self.id, states, self.symbols, states[self.initial_state.id])

    def __repr__(self):
        states = [state for state in self.states]
        final_states = [state for state in self.states if self.states[state].is_final]
        id = self.id + '=(' + str(states) + ',' + str(self.symbols) + ',' + self.initial_state.id + ',' + str(final_states) + ')'
        
        transitions = []
        for state in self.states:
            for transition in self.states[state].transitions:
                transitions.append((state,transition,self.states[state].transitions[transition]))
        
        str_transitions = ''
        for transition in transitions:
            str_transitions += str(transition) + '\n' 

        return id + '\n' + str_transitions