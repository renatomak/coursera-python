def prime(num):
  for dividend in range(2, num):
    if num % dividend == 0:
      return False
  return True

# print(prime(9))


def maior_primo(num):
  for valor in reversed(range(2, num+1)):
    if prime(valor):
      return valor


