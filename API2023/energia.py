def main():
    consumidor = ''
    consumo_kwh = 0
    valor_cem = 0
    bandeira = 0
    n_familias = int(input('Número de famílias:' ))

    while n_familias > 0:
        consumidor = input('Nome do consumidor: ')
        consumo_kwh = float(input('Consumo de KWh: '))
        valor_cem = 8

        consumo_rs = calcular_consumo(consumo_kwh, valor_cem)
        bandeira_tarifaria = calcular_bandeira(bandeira, consumo_rs, valor_cem)
        s_imposto = consumo_rs + bandeira_tarifaria
        iluminacao = calc_tarifa(consumo_kwh, consumo_rs)
        icms = calc_icms(consumo_rs)
        cofins = calc_cofins(consumo_rs)

        total = s_imposto + iluminacao + icms + cofins


    



        print('****** TALÃO MENSAL XPTO ********')
        print(f'Consumidor: {consumidor}')
        print(f'Consumo (KWh): {consumo_kwh}')
        print(f'Consumo (R$): R$ {consumo_rs:.2f} (valor por KWh: R$ {valor_um:.2f})')
        print(f'Bandeira Tarifária: R$ {bandeira_tarifaria:.2f} (valor por 100KWh: R$ {valor_cem:.2f})')
        print(f'Total sem Impostos: R$ {s_imposto:.2f}')
        print(f'ICMS: R$ {icms:.2f}')
        print(f'PIS/COFINS: R$ {cofins:.2f}')
        print(f'Iluminação Pública: R$ {iluminacao:.2f}')
        print('—-----------—-----------—-----------—-----------')
        print(f'Total a Pagar: R$ {total:.2f}')

        n_familias -= 1

def calcular_consumo(c, v):
    if c < 30:
        kwh = 0
    elif c < 100:
        kwh = (c * 0.59) * v
    else:
        kwh = (c * 0.75) * v

    return kwh
        

def calcular_bandeira(b, kwh, cem):
    valor_cem = kwh * cem
    return valor_cem * b


def calc_tarifa(c, r):
    if c > 80:
        return r * 0.06
    else:
        return 0



def calc_icms(c):
    return c * 0.25


def calc_cofins(c):
    return c * 0.0375


main()