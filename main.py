import sys
import argparse
import queue
from Automaton import Automaton
from CompostState import CompostState
from State import State

afnd_automaton = None
afd_automaton = None

def handle_arguments():
  parser = create_parse()
  args = parser.parse_args()

  file_path = args.file

  return file_path


def create_parse():
  parser = argparse.ArgumentParser(prog='Autômatos')
  parser.add_argument('-file', required=True, type=str)

  return parser

def loadAutomaton():
  file_path = input('Insira o nome do arquivo a ser carregado: ')

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
    print("Erro ao carregar o arquivo "+file_path)
    return None
  

def create_automaton(auto_id, states_list, symbols_list, init_state, final_states_list, transitions_list):
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

def write_automaton(automaton):
  with open('AFD-'+automaton.id+'.txt', 'w+') as file:
    for state in automaton.states:
      for transition in automaton.states[state]:
        line = '('+state+','+transition+')='+automaton.states[state].transitions[transition]
        file.write(file)
        file.flush()


def print_menu():
  global afd_automaton, afnd_automaton

  print('\nAutomatos:')
  print('AFND -> ', 'Ok!' if afnd_automaton else 'None')
  print('AFD -> ', 'Ok!' if afd_automaton else 'None')

  print('\nEscolha uma ação:')
  print('\n[1] .......... Carregar autômato de arquivo texto.')
  print('[2] .......... Converter AFND para AFD.')
  print('[3] .......... Validar palavras.')
  print('[4] .......... Validar arquivo de palavras.\n')

def main():
  global afd_automaton, afnd_automaton

  while True:
    print_menu()
    choice = input('-> ')

    if choice == '0':
      break
    elif choice == '1':
      afnd_automaton = loadAutomaton()
      if afnd_automaton:
        print('Automaton carregado com sucesso!')

if __name__== "__main__":
  main()