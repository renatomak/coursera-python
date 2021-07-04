n = input('Digite um número inteiro:')

def add_digits(num):
  result = 0
  for x in num:
    result += int(x)
  return result

print(add_digits(n))