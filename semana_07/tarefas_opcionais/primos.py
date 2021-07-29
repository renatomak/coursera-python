from functools import reduce

def find_all_multiple(n):
  return [ multiple for multiple in range(1, n+1) if n % multiple == 0]


def n_primos(num):
    count = 0
    for n in range(2, num+1):
        if len(find_all_multiple(n)) == 2:
            count += 1
    return count

print(n_primos(121))