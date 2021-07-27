altura_retangulo = int(input())
largura_retangulo = int(input())

for altura in range(altura_retangulo):
    for largura in range(largura_retangulo):
        if altura == 0 or altura == altura_retangulo -1:
            print("#", end='')
        else:
            if largura == 0 or largura == largura_retangulo -1:
                print("#", end='')
            else: 
                print(' ', end='')
    print()