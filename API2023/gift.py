def main():
    nome_cliente = ''
    maior = 0
    menor = None

    quant_compras = 0
    contador = 0
    compra = 0
    compra_s_cash = 0
    somatorio_compras = 0
    n = int(input('Quantidade de clientes: '))

    def calcular_cashback(valor_compra):
        if valor_compra < 250:
            cashback = valor_compra * 0.05
        elif valor_compra < 500:
            cashback = ((valor_compra - 250) * 0.07) + (valor_compra)
        elif valor_compra < 750:
            cashback = valor_compra * 0.92
        else:
            # valor_acumulado = (valor_compra * 0.95)
        
        return cashback


    while n > 0:
        n -= 1
        nome_cliente = input('Nome do cliente: ')
        quant_compras = int(input(f'Quantidade de compras do cliente {nome_cliente} : '))

        while contador < quant_compras:
            compra = float(input('Preço da compra:'))
            compra_s_cash += compra
            compra = calcular_cashback(compra)

            if compra > maior:
                maior = compra
            
            if compra < menor:
                menor = compra

            somatorio_compras += compra
            contador += 1
            

    cash = somatorio_compras - compra_s_cash
    investimento = (cash * somatorio_compras) * 100

    valor_medio = somatorio_compras / n

    print(f'Faturamento: {somatorio_compras:.2f} R$.')
    # print(f'Distribuição em cashback: ')
    print(f'Valor em R$ de investimento: {cash:.2f} R$.')
    print(f'Valor em % de investimento: {investimento:.2f} %')
    print(f'Maior valor pago em cashback: {maior} R$.')
    print(f'Menor valor pago em cashback: {menor} R$.')
    print(f'Valor médio pago em cashback: {valor_medio} R$.')

main()