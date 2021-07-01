import math

a = int(input())
b = int(input())
c = int(input())

delta = (b**2) - (4*a*c)

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz = math.sqrt((b**2) - (4*a*c))
    x = (b + raiz)/(2*a)
    print('a raiz desta equação é', x)
else:
    raiz = math.sqrt((b**2) - (4*a*c))
    x1 = (b + raiz)/(2*a)
    x2 = (b - raiz)/(2*a)
    if x1 < x2:
        print('as raízes da equação são', x1, 'e', x2)
    else:
        print('as raízes da equação são', x2, 'e', x1)
