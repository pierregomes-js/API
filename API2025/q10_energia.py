def main():
    n_familias = int(input('Número de famílias:' ))

    while n_familias > 0:
        Consumidor = input('Nome do consumidor: ')
        consumo_kwh = float(input('Consumo de KWh: '))

        consumo_rs = calcular_consumo(consumo_kwh)
        bandeira_tarifaria = calcular_bandeira(consumo_rs, consumo_kwh)





    print('****** TALÃO MENSAL XPTO ********')
    print(f'Consumidor: {consumidor}')
    print(f'Consumo (KWh): {consumo_kwh}')
    print(f'Consumo (R$): R$ {consumo_rs}(valor por KWh: R$ {valor_kwh})')
    print(f'Bandeira Tarifária: R$ {bandeira_tarifaria} (valor por 100KWh: R$ {valor_100kwh})')
    print(f'Total sem Impostos: R$ {total_s_imposto}')
    print(f'ICMS: R$ {icms}')
    print(f'PIS/COFINS: R$ {cofins}')
    print(f'Iluminação Pública: R$ {iluminacao}')
    print('—-----------—-----------—-----------—-----------')
    print(f'Total a Pagar: R$ {total}')

def calcular_consumo(c):
    return c * 0.89

def calcular_bandeira(rs, kwh):
    if kwh < 30:
        return kwh * 0
    



main()