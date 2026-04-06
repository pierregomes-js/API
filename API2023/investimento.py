
def main():
    meses = 0
    objetivo = float(input('Objetivo: '))
    valor_necessario = float(input('Valor para realizá-lo: '))

    salario = float(input('Salário: '))
    percentual_investimento = float(input('Percentual de investimento: '))
    percentual_investimento /= 100

    valor_salario = salario / percentual_investimento

    taxa_juros = float(input('Taxa de juros: '))
    taxa_juros /= 100

    while valor_acumulado < objetivo:
        meses += 1
        valor_acumulado += valor_salario
        valor_salario = valor_salario / percentual_investimento
        valor_necessario -= valor_acumulado

    print(meses)

main()