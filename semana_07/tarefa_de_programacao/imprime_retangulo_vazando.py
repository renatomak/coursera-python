altura_retangulo = int(input('digite a largura: '))
largura_retangulo = int(input('digite a altura: '))

for largura in range(largura_retangulo):
    for altura in range(altura_retangulo):
        if altura == 0 or altura == altura_retangulo - 1:
            print("#", end='')
        else:
            if largura == 0 or largura == largura_retangulo - 1:
                print("#", end='')
            else:
                print(' ', end='')
    print()
