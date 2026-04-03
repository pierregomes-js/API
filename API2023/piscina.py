def main():
    largura = float(input('Largura da piscina: '))
    comprimento = float(input('Comprimento da piscina: '))
    profundidade = float(input('Profundidade da piscina: '))
    valor = float(input('Digite o valor por litros: '))
    dimensao = largura * comprimento * profundidade
    capacidade_max = dimensao / 1000
    litros_totais = capacidade_max * 0.85

    valor_total = calcular_valor(valor, litros_totais)
    
    print(f'Capacidade máxima da piscina: {capacidade_max:.2f}l. ')
    print(f'Recomendação de quantidade de litros: {litros_totais:.2f}l.')
    print(f'Valor total a ser pago: {valor_total:.2f}R$.')

def calcular_valor(valor, litros_totais):
    litros = 0

    while litros_totais > 0:
        litros += 1
        litros_totais -= 1000

    return valor * litros

main()