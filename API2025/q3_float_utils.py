
def receber_decimal(texto):
    try:
        numero = float(input(texto))
    except:
        while True:
            print('Número inválido, digite outro número.')
            numero = float(input(texto))
    return numero
    

def receber_decimal_positivo(texto):
    numero = receber_decimal(texto)

    while numero < 0:
        print('Número inválido.')
        numero = receber_decimal(texto)

    return numero
    

def receber_decimal_min(texto, minimo):
    numero = receber_decimal(texto)
    while numero < minimo:
        print(f'Número inválido, digite no mínimo {minimo}.')
        numero = receber_decimal(texto)

    return numero


def receber_inteiro_max(texto, maximo):
    numero = receber_decimal(texto)
    while numero > maximo:
        print(f'Número inválido, digite no máximo {maximo}.')
        numero = receber_decimal(texto)

    return numero
    
    
def receber_intervalo(texto, minimo, maximo):
    numero = receber_decimal(texto)

    while (numero < minimo or numero > maximo):
        print(f'Número inválido, digite no mínimo {minimo} e no máximo {maximo}.')
        numero = receber_decimal(texto)
    return numero
