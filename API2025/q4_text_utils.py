
def receber_texto(conteudo):
    texto = input(conteudo)
    return texto

def receber_texto_min(conteudo, minimo):
    texto = input(conteudo)

    while len(texto) < minimo:
        print(f'Texto inválido, digite no mínimo {minimo} dígitos.')
        texto = input(conteudo)

    return texto
    

def receber_texto_max(conteudo, maximo):
    texto = input(conteudo)

    while len(texto) > maximo:
        print(f'Texto inválido, digite no máximo {maximo} dígitos.')
        texto = input(conteudo)

    return texto

def receber_intervalo(conteudo, minimo, maximo):
    texto = input(conteudo)

    while (len(texto) < minimo) or (len(texto) > maximo):
        print(f'Número inválido, digite no mínimo {minimo} dígitos e no máximo {maximo} dígitos.')
        texto = input(conteudo)
    return texto