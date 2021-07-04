n = int(input('Digite o valor de n:'))

def odd(num):
  i = 0
  j = 1
  while (i < num):
    if (j % 2 != 0):
      print(j)
      i+=1
    j+=1

odd(n)
