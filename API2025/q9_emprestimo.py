def main():
    renda_mensal = float(input('Renda mensal: '))
    valor_desejado = float(input('Valor do empréstimo desejado:'))
    prazo_desejado = float(input('Valor do prazo desejado: '))

    selic = 14.75
    eh_valido = validar_emprestimo(renda_mensal, valor_desejado)
    iof = calcular_iof(valor_desejado, prazo_desejado, selic)
    juros = calcular_juros(iof, valor)
    montante = juros + valor_desejado

    print('Resultado:')
    print(f'Valor do IOF: {}.')
    print(f'Valor dos juros a pagar: {}.')
    print(f'Valor Total a pagar: {}.')
    print(f'Valor da Parcela Mensal: {}.')
    #emprestimo aprovado ou reprovado

def validar_emprestimo(renda, valor):
    if valor < 1518:
        return False
    elif valor > (renda * 0.3):
        return False
    else:
        return True


main()