MSG_INIT = """Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato 2"""

def find_all_multiple(n):
  return [ multiple for multiple in range(1, n+1) if n % multiple == 0]

def check_multiple(n, m):
  list_multiple = find_all_multiple(n)
  return True if m in list_multiple else False


def pc_game(n, m):
  game = n % (m+1)
  if game == 0:
    game = m
  
  print(f'\nO computador tirou {game} peça.')

  return n-game

def user_game(n, m):
  game = 0

  while game == 0:
    game = int(input('\nQuantas peças você vai tirar? '))
    if game <= 0 or game > m:
      print('\nOops! Jogada inválida! Tente de novo.')
      game = 0

  print(f'Você tirou {game} peça.')
  return n-game


def game_round(count):
  print(f'**** Rodada {count} ****')
  n = int(input('Quantas peças? '))
  m = int(input('Limite de peças por jogada? '))
  
  pc_start = check_multiple(n, m)

  if pc_start:
    print('\nComputador começa!')
  else:
    print('\nVoce começa!')
  
  play_now = pc_start

  while n > 0:
    if play_now:
      n = pc_game(n, m)
      play_now = False
    else:
      n = user_game(n, m)
      play_now = True
    
    if n == 0:
      print('Fim do jogo! O computador ganhou!')
    else:
      print(f'Agora restam {n} peças no tabuleiro.')



def game_nim():
  print(MSG_INIT)
  choice = int(input())
  if choice == 1:
    print('Você escolheu uma partida isolada')
    game_round(1)
  elif choice == 2:
    count = 1
    print('Voce escolheu um campeonato!')
    while count <= 3:
      game_round(count)
      count += 1
    print('\n**** Final do campeonato! ****')
    print('\nPlacar: Você 0 X 3 Computador')


game_nim()
