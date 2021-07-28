MSG_INIT = """Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato """

def find_all_multiple(n):
  return [ multiple for multiple in range(1, n+1) if n % multiple == 0]

def check_multiple(n, m):
  list_multiple = find_all_multiple(n)
  return True if m in list_multiple else False


def computador_escolhe_jogada(n, m):
  if n <= m:
    return n
  else:
    move = n % (m+1)
    if move > 0:
      return move
  return m


def usuario_escolhe_jogada(n, m):
  move = 0

  while move == 0:
    move = int(input('\nQuantas peças você vai tirar? '))
    if move > m or move <= 0:
      print('\nOops! Jogada inválida! Tente de novo.')
      move = 0

  print(f'Você tirou {move} peça.')
  return move


def partida():
  n = int(input('Quantas peças? '))
  m = int(input('Limite de peças por jogada? '))
  
  pc_start = n % (m+1)

  if pc_start:
    print('\nComputador começa!')
  else:
    print('\nVoce começa!')
  
  play_now = pc_start

  while n > 0:
    if play_now:
      move = computador_escolhe_jogada(n, m)
      print(f'\nO computador tirou {move} peça.')
      play_now = False
    else:
      move = usuario_escolhe_jogada(n, m)
      play_now = True
    
    n -= move
    if n == 0:
      print('Fim do jogo! O computador ganhou!')
    else:
      print(f'Agora restam {n} peças no tabuleiro.')
    

def compeonato():
  round = 1
  while round <= 3:
    print(f'**** Rodada {round} ****')
    partida()
    round += 1
  
  print('\n**** Final do campeonato! ****')
  print('\nPlacar: Você 0 X 3 Computador')


if __name__ == '__main__':
  print(MSG_INIT)
  choice = 0

  choice = int(input())
  if choice == 1:
    print('Você escolheu uma partida isolada')
    partida()
  elif choice == 2:
    count = 1
    print('Voce escolheu um campeonato!')
    compeonato()

