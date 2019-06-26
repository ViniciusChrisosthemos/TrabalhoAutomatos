import sys
from src.Manager import Manager

load_file = 'lf'
convert = 'c'
validate_word = 'vw'
validate_words = 'vws'
print_option = 'p'
help_option = 'help'
exit_option = 'exit'

def print_menu():
  print('\nComandos:')
  print(f'\n[{load_file}]   .......... Carregar autômato de arquivo texto.')
  print(f'[{convert}]    .......... Converter AFND para AFD.')
  print(f'[{validate_word}]   .......... Validar palavras.')
  print(f'[{validate_words}]  .......... Validar arquivo de palavras.')
  print(f'[{print_option}]   .......... Exibir autômato.')
  print(f'[{help_option}] .......... Exibe comandos.')
  print(f'[{exit_option}] .......... Fechar programa.')

def main():
  manager = Manager()
  print_menu()

  while True:
    try:
      choice = []
      choice = input('\n-> ').split(' ')
      try:
        if choice[0] == load_file:
          try:    
            manager.load_automaton(choice[1])
            print('\nRESULTADO: Autômato carregado com sucesso!')
          except FileNotFoundError:
            print(f'\nRESULTADO: Arquivo {choice[1]} não encontrado.')
          except RuntimeError:
            print('\nRESULTADO: Ocorreu um erro ao carregar o autômato.')

        elif choice[0] == validate_word:
          try:
            print('\nRESULTADO: ', manager.validate_word(choice[1]))
          except RuntimeError:
            print('\nRESULTADO: Ocorreu um erro ao validar a palavra.')
        
        elif choice[0] == validate_words:
          if not manager.automaton:
            print('\nRESULTADO: Autômato não carregado!')
          else:
            try:
              manager.load_words(choice[1])
              result = manager.validate_words()
              print('\nRESULTADO: ')

              for word in result:
                print(word, '->', result[word])

            except FileNotFoundError:
              print(f'\nRESULTADO: Arquivo {choice[1]} não encontrado.')
  
        elif choice[0] == convert:
          try:
            manager.converts_afnd_to_afd()
            print('\nRESULTADO: Conversão concluida com sucesso!')
          except RuntimeError:
            print('\nRESULTADO: Ocorreu um erro ao converter o AFND.')

        elif choice[0] == print_option:
          print(manager.automaton)

        elif choice[0] == help_option:
          print_menu()

        elif choice[0] == exit_option:
          break
        
        else:
          print(f'\nRESULTADO: Comando {choice[0]} não existe!')
      except RuntimeError:
        print('\nErro ao processar o comando.\n')
    except IndexError:
      print('\nRESULTADO: Quantidade de argumentos inválido para a ação escolhida.')

if __name__== "__main__":
  main()