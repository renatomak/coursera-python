def factorial(num):
  if(num == 1 or num <= 0):
    return 1
  else:
    return num*factorial(num-1)

def binomial(n, k):
  if k <= n:
    if (n == k or (k == 0 == n)):
      return 1
    if k == 1:
      return n
    return factorial(n) / (factorial(k) * factorial(n-k))
  else:
    print('Erro de parametros')