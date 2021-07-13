def find_all_multiple(n):
  return [ multiple for multiple in range(1, n+1) if n % multiple == 0 ]



""" Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato 2

Voce escolheu um campeonato!

**** Rodada 1 ****

Quantas peças? 3
Limite de peças por jogada? 1

Computador começa!

O computador tirou uma peça.
Agora restam 2 peças no tabuleiro.

Quantas peças você vai tirar? 2

Oops! Jogada inválida! Tente de novo.

Quantas peças você vai tirar? 1

Você tirou uma peça.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

**** Rodada 2 ****

Quantas peças? 3
Limite de peças por jogada? 2

Voce começa!

Quantas peças você vai tirar? 2 
Voce tirou 2 peças.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

**** Rodada 3 ****

Quantas peças? 4
Limite de peças por jogada? 3

Voce começa!

Quantas peças você vai tirar? 2
Voce tirou 2 peças.
Agora restam 2 peças no tabuleiro.

O computador tirou 2 peças.
Fim do jogo! O computador ganhou!

**** Final do campeonato! ****

Placar: Você 0 X 3 Computador """