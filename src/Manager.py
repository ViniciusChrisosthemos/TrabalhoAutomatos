from src.State import State
from src.CompostState import CompostState
from src.Automaton import Automaton

class Manager:

    def __init__(self):
        self.automaton = None
        self.words = []

    def converts_afnd_to_afd(self):
        self.automaton = self.automaton.to_afd()

    def validate_word(self, word):
        return self.automaton.validate_word(word)

    def validate_words(self):
        result = {}

        for word in self.words:
            result[word] = self.automaton.validate_word(word)

        return result

    def load_words(self, file_path):
        with open(file_path, 'r') as file:
            self.words = file.read().splitlines()


    def create_automaton(self, auto_id, states_list, symbols_list, init_state, final_states_list, transitions_list):
        auto_id = auto_id[0]
        
        states = {}
        for id in states_list:
            states[id] = State(id, False, {})
        
        init_state = states[init_state]

        for id in final_states_list:
            states[id].is_final = True
        
        for transition in transitions_list:
            origin = transition[0]
            symbol = transition[1]
            destiny = transition[2]

            if symbol not in states[origin].transitions:
                states[origin].transitions[symbol] = []

            states[origin].transitions[symbol].append(destiny)

        return Automaton(auto_id, states, symbols_list, init_state)

    def load_automaton(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.read().split('\n')

            auto_info = lines[0]
            transitions = lines[2:]

            auto_info = auto_info.replace("=({",";")\
                                .replace("},{", ";").replace("},", ";")\
                                .replace(",{", ";").replace("})", "")
            auto_info = [info.split(",") for info in auto_info.split(";")]

            id = auto_info[0]
            states = auto_info[1]
            symbols = auto_info[2]
            init_state = auto_info[3][0]
            final_states = auto_info[4]

            trans_formated = []
            for transition in transitions:
                transition = transition.replace("(", "").replace(")=", ",")
                trans_formated.append(transition.split(",")) 

            self.automaton = self.create_automaton(id, states, symbols, init_state, final_states, trans_formated)
        except RuntimeError:
            raise Exception('Erro ao carregar o autômato.')

    def write_automaton(self, automaton):
        try:
            with open('AFD-'+automaton.id+'.txt', 'w+') as file:
                for state in automaton.states:
                    for transition in automaton.states[state]:
                        line = '('+state+','+transition+')='+automaton.states[state].transitions[transition]
                        file.write(line)
                        file.flush()
        except RuntimeError:
            raise Exception('Erro ao escrever o autômaton.')