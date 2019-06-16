import sys
import argparse
from Automaton import Automaton
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
  pass

def create_automaton(id, states_list, symbols_list, init_state, final_states_list, transitions_list):
  states = {}
  for id in states_list:
    states[id] = State(id)
  
  init_state = states[init_state]

  for id in final_states_list:
    states[id].is_final = True
  
  # Processa as transições
  print(states)
  return None

  

def main():
  file_path = handle_arguments()
  
  with open(file_path, 'r') as file:
    lines = file.read().split('\n')

  print(lines)
  # automaton = create_automaton(automaton_info)
  pass
  
if __name__== "__main__":
  #main()
  string = "a=({q0,q1,q2},{a,b,c},q0,{q1,q2})".replace("=({",";")\
                                              .replace("},{", ";").replace("},", ";")\
                                              .replace(",{", ";").replace("})", "")

  create_automaton("asd", ["q0","q1","q2","q3"], [], "q1", ["q2","q3"], [])

  print(string)
