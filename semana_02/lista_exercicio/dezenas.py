entrance = input("Digite um número inteiro: ")
entrace_float = float(entrance)
resto_dezena_milhar = entrace_float % 10000
resto_unidade_milhar = resto_dezena_milhar % 1000
resto_centena = resto_unidade_milhar % 100
dezena = int(resto_centena // 10)
print("O dígito das dezenas é", dezena)