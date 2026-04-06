
def receber_inteiro(texto):
    try:
        numero = int(input(texto))
    except:
        while True:
            print('Número inválido, digite outro número.')
            numero = int(input(texto))
    return numero
    

def receber_inteiro_positivo(texto):
    numero = receber_inteiro(texto)

    while numero < 0:
        print('Número inválido.')
        numero = receber_inteiro(texto)

    return numero
    

def receber_inteiro_min(texto, minimo):
    numero = receber_inteiro(texto)
    while numero < minimo:
        print(f'Número inválido, digite no mínimo {minimo}.')
        numero = receber_inteiro(texto)

    return numero


def receber_inteiro_max(texto, maximo):
    numero = receber_inteiro(texto)
    while numero > maximo:
        print(f'Número inválido, digite no máximo {maximo}.')
        numero = receber_inteiro(texto)

    return numero
    
    
def receber_intervalo(texto, minimo, maximo):
    numero = receber_inteiro(texto)

    while (numero < minimo or numero > maximo):
        print(f'Número inválido, digite no mínimo {minimo} e no máximo {maximo}.')
        numero = receber_inteiro(texto)
    return numero
