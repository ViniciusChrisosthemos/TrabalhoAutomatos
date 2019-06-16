import sys
import argparse
from Automaton import Automaton


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

def create_automaton(automaton_info):
  return None

  

def main():
  file_path = handle_arguments()
  
  with open(file_path, 'r') as file:
    lines = file.read().split('\n')

  print(lines)
  # automaton = create_automaton(automaton_info)
  pass
  
if __name__== "__main__":
  main()
