def main():

    leitura_atual = int(input('Leitura atual: '))
    leitura_anterior = int(input('Leitura anterior: '))


    consumo = leitura_atual - leitura_anterior
    consumo_rs = calcular_consumo(consumo)
    bandeira = calcular_bandeira(consumo_rs)
    cofins = calc_cofins(consumo_rs)
    icms = calc_icms(consumo_rs)
    iluminacao = calc_tarifa(consumo, consumo_rs)
    total = consumo_rs + bandeira + cofins + icms + iluminacao



    print('Total: ')
    print(f'Consumo em KWh: {consumo} KWh.')
    print(f'Valor faturado: {consumo_rs:.2f} R$.')
    print(f'Bandeira: {bandeira:.2f} R$. (Valor por 100KWh: 8,00 R$).')
    print(f'ICMS: {icms:.2f} R$.')
    print(f'PIS/COFINS: {cofins:.2f} R$')
    print(f'Taxa de iluminação: {iluminacao:.2f} R$.')
    print(f'Total: {total:.2f} R$')




def calcular_consumo(c):
    if c < 30:
        kwh = 0
    elif c < 100:
        kwh = (c * 0.59)
    else:
        kwh = (c * 0.75)

    return kwh
        

def calcular_bandeira(rs):
    return (rs / 100) * 8


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