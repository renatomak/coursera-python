import tarefa.jogo_min as game

def test_find_all_multiple_zero():
  assert game.find_all_multiple(0) == []

def test_find_all_multiple_par():
  assert game.find_all_multiple(8) == [1, 2, 4, 8]

def test_find_all_multiple_impar():
  assert game.find_all_multiple(21) == [1, 3, 7, 21]

def test_find_all_multiple_primo():
  assert game.find_all_multiple(19) == [1, 19]