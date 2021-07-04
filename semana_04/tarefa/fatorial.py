n = int(input('Digite o valor de n:'))

""" def fatorial(num):
  if(num == 1):
    return 1
  else:
    return num*fatorial(num-1) """
def fatorial(num):
  i=2
  result = 1
  while(i <= num):
    result *=i
    i+=1
  return result

print(fatorial(n))