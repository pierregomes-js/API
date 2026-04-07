def main():
    contador_produtos = 0
    soma = 0
    parte_cima = '——- PESQUISA DE PREÇOS —---'
    opcao = int(input(menu()))

    while opcao != 3:
        if opcao == 1:
            contador_produtos += 1
            desc = input('Descrição: ')
            esp = int(input('Especificação: '))
            valor_ponto = float(input('Valor: '))
            soma += valor_ponto
            somatorio = converter(soma)

            linha = f'\n{contador_produtos} - {desc} ({esp} kg) R$ {converter(valor_ponto)}'

            parte_baixo = f'''
—--------------------------
Valor total:       R$ {somatorio}'''

            parte_cima += linha

            opcao = int(input(menu()))


        if opcao == 2:

            pesquisa = parte_cima + parte_baixo
            print(pesquisa)
            opcao = int(input(menu()))

#fora do while
    valor_total = soma
    forma = int(input(pagamento()))
    parcela = calcular_parcela(forma, valor_total)

#condicao indesejada
    while forma == 2 and valor_total < 30:
        print('Não será possível parcelar a compra. ')
        forma = int(input(pagamento()))

#formas
    if forma == 3:
        print(f'Valor total: {converter(juros_compostos(valor_total))} \n Valor da parcela: {converter(parcela)}')
    elif forma == 2:
        print(f'Valor total: {converter(valor_total)} \nValor da parcela: {converter(parcela)}')
    else:
        print(f'Valor total: {converter(valor_total)}')
    

#funcoes 

def calcular_parcela(forma, valor_total):
    if forma == 2 and valor_total > 30:
        if valor_total < 100:
            parcela = valor_total / 3
        else:
            parcela = valor_total / 5
    else:
        parcela = juros_compostos(valor_total) / 6
    return parcela

def menu():
    return '''\n Menu
    1 - Incluir Item
    2 - Imprimir lista
    3 - Sair \n : '''

def converter(valor):
    decimal = (valor - int(valor)) * 100
    if decimal == 0:
        decimal = '00'
        return f'{int(valor)},{decimal}'
    else:
        return f'{int(valor)},{decimal:.0f}'

def pagamento():
    return '''Formas de pagamento:
    1 - À vista
    2 - Parcelado sem Juros(apenas valores acima de 30)
    3 - Parcelado 6x com Juros compostos \n: '''

def juros_compostos(valor):
    mes = 1
    meses = 6
    taxa = 0.05
    while mes <= meses:
        valor = valor + (valor * taxa)
        mes += 1
    return valor


main()