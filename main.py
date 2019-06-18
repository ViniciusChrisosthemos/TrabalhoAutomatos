import sys
import argparse
import queue
from Automaton import Automaton
from CompostState import CompostState
from State import State

def handle_arguments():
  parser = create_parse()
  args = parser.parse_args()

  file_path = args.file

  return file_path


def create_parse():
  parser = argparse.ArgumentParser(prog='Autômatos')
  parser.add_argument('-file', required=True, type=str)

  return parser

def loadAutomaton(file_path):
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

    return create_automaton(id, states, symbols, init_state, final_states, trans_formated)

  except RuntimeError:
    print("Error")
  

  pass

def create_automaton(auto_id, states_list, symbols_list, init_state, final_states_list, transitions_list):
  auto_id = auto_id[0]
  
  states = {}
  for id in states_list:
    states[id] = State(id)
  
  init_state = states[init_state]

  for id in final_states_list:
    states[id].is_final = True
  
  for transition in transitions_list:
    origin = transition[0]
    symbol = transition[1]
    destiny = transition[2]
    if symbol not in states[origin].transitions:
      states[origin].transitions[symbol] = []

    states[origin].transitions[symbol].append(states[destiny])

  return Automaton(auto_id, states, symbols_list, init_state)

  

def main():
  file_path = handle_arguments()
  automaton = loadAutomaton(file_path)

  print(automaton)
  afnd_to_afd(automaton)

def afnd_to_afd(afnd):
  mqueue = queue.Queue()
  new_states = {}

  mqueue.put(CompostState([afnd.initial_state]))

  while not mqueue.empty():
    c_state = mqueue.get()

    for symbol in afnd.symbols:
      temp_state = CompostState(c_state.get_transitions(symbol))

      if temp_state.id in new_states:
        c_state.transitions[symbol] = new_states[temp_state.id]
      else:
        c_state.transitions[symbol] = temp_state
        mqueue.put(temp_state)
    
    new_states[c_state.id] = c_state
  
  print(new_states['q0'].get_state())
    

if __name__== "__main__":
  main()