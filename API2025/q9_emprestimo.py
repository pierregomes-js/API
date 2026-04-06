def main():
    renda_mensal = float(input('Renda mensal: '))
    valor_emprestimo = float(input('Valor do empréstimo :'))
    prazo = float(input('Valor do prazo desejado: '))

    selic = 14.75
    iof = calcular_iof(valor_emprestimo, prazo)
    emprestimo_juros = valor_emprestimo + iof
    juros = calcular_juros(emprestimo_juros, selic, prazo)
    parcela = juros / prazo
    eh_valido = validar_emprestimo(renda_mensal, parcela)

    print('Resultado:')
    print(f'Valor do IOF: {}.')
    print(f'Valor dos juros a pagar: {}.')
    print(f'Valor Total a pagar: {}.')
    print(f'Valor da Parcela Mensal: {}.')
    #emprestimo aprovado ou reprovado

def calcular_iof(e, p):
    valor = e * (1 - 0.038)
    dia = (30 * p) * (1 - 0.00082)
    return valor + dia

def calcular_juros(v, s, p):
    if p <= 6:
        j = v * (s * 0.5) 
    elif p <= 12:
        j = v * (s * 0.75)
    elif p <= 18:
        j = v * s
    else:
        j = v * (s * 1.30)

    return j


def validar_emprestimo(r, p):
    minimo = 1518
    maximo = r * 0.30

    if p > maximo or p < minimo:
        return 



main()