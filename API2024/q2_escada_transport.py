def main():
    sexo = input('Insira o sexo (F ou M): ')
    perda_peso = float(input('Insira a quantidade de kg que deseja perder: '))
    qtd_dias = int(input('Insira a quantidade de dias por semana de treino: '))
    qtd_horas = int(input('Insira a quantidade de horas de treino para cada dia de exercício: '))
    proporcao_transport = float(input('Insira a proporção (%) de tempo alocado ao Transport: '))
    proporcao_escada = float(input('Insira a proporção (%) de tempo alocado a escada: '))

    
    minutos = qtd_horas * 60
    minutos_semanais = qtd_dias * minutos
    calorias = calcular_calorias(sexo, perda_peso)
    minutos_transport = calcular_minutos(minutos, proporcao_transport)
    minutos_escada = calcular_minutos(minutos, proporcao_escada)
    gasto_escada = calcular_gasto('escada', minutos_escada, sexo)
    gasto_transport = calcular_gasto('transport', minutos_transport, sexo)
    gasto_diario = gasto_transport + gasto_escada
    qtd_semanas = calcular_semanas(minutos_semanais, gasto_diario, calorias)

    print('Resultado: ')
    print(f'Quantidade de semanas para se obter o resultado: {qtd_semanas}')
    print(f'Minutos de transport diários: {minutos_transport}')
    print(f'Minutos de escada diários: {minutos_escada}')

def calcular_calorias(sexo, perda_peso):
    if sexo == 'F':
        return (perda_peso * 7000) + 2000
    else:
        return (perda_peso * 7000) + 2400
    

def calcular_minutos(minutos, proporcao):
    return minutos * (proporcao / 100)

def calcular_gasto(exercicio, minutos_exercicio, sexo):
    if exercicio == 'escada':
        if sexo == 'F':
            gasto = (minutos_exercicio / 8) * 100
        else:
            gasto = (minutos_exercicio / 7) * 100
    else:
        if sexo == 'F':
            gasto = (minutos_exercicio / 6) * 100
        else:
            gasto = (minutos_exercicio / 5) * 100
    return gasto 

def calcular_semanas(minutos_semanais, gasto_diario, calorias):
    semanas = 1
    gasto_semanal = minutos_semanais * gasto_diario
    while gasto_semanal < calorias:
        semanas += 1
        gasto_semanal += gasto_semanal
    return semanas



main()
#separar em horas e minutos