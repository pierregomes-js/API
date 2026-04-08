
def main():
    meses = 0
    objetivo = input('Digite seu Objetivo: ')
    valor_necessario = float(input('Valor para realizá-lo: '))

    salario = float(input('Salário: '))
    percentual_investimento = float(input('Percentual de investimento: '))
    percentual_investimento /= 100

    valor_investido = salario / percentual_investimento

    taxa_juros = float(input('Taxa de juros: '))
    taxa_juros /= 100

    while valor_investido < valor_necessario:
        meses += 1
        valor_investido = valor_investido + (1 + taxa_juros) ** meses

    if meses >= 12:
        anos = meses // 12
        meses = meses % 12
        print(f'Seu objetivo será alcançado em {anos} anos e {meses} meses. ')
    else:
        print(f'Seu objetivo será alcançado daqui a {meses} meses.')

main()