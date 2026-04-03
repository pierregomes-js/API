def main():

    maior_nota = 0
    menor_nota= 0
    nota_mulheres = 0
    nota_homens = 0
    somatorio_nota = 0
    somatorio_alunos = 1
    somatorio_homens = 0
    somatorio_mulheres = 0
    nota = 0

    sexo = input('Sexo (M ou F): ')
    sexo = sexo.upper()

    while sexo != 'F' and sexo != 'M':
        nota = int(input('Nota (1 a 10): '))

        somatorio_nota += nota
        somatorio_alunos += 1

        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

        if sexo == 'F':
            nota_mulheres += nota
            somatorio_mulheres += 1
        else:
            nota_homens += nota
            somatorio_homens += 1

        sexo = input('Sexo (M ou F): ')

    media_nota = somatorio_nota / somatorio_alunos

    porcent_homens = calcular_perfomance(nota_homens, somatorio_homens)
    porcent_mulheres = calcular_perfomance(nota_mulheres, somatorio_mulheres)
    desempenho_total = calcular_desempenho(media_nota, somatorio_alunos)
    desempenho_homens = calcular_desempenho(nota_homens, somatorio_alunos)
    desempenho_mulheres = calcular_desempenho(nota_mulheres, somatorio_mulheres)




    print(f'Maior nota geral: {maior_nota}.')
    print(f'Menor nota geral: {menor_nota}.')
    print(f'Média geral: {media_nota}.')
    print(f'Média geral: {media_nota}.')
    print(f'Perfomance da nota dos homens: {porcent_homens}%.')
    print(f'Perfomance da nota das mulheres: {porcent_mulheres}%.')

    print(f'Total de alunos: {somatorio_alunos}.')
    print(f'Total de mulheres: {somatorio_mulheres}.')
    print(f'Total de homens: {somatorio_homens}.')
    print(f'Desempenho total da turma: {desempenho_total}.')
    print(f'Desempenho dos homens: {desempenho_homens}.')
    print(f'Desempenho das mulheres = {desempenho_mulheres}.')

    def calcular_perfomance(nota, somatorio):
        perfomance =  (nota / somatorio) * 100
        return f'{perfomance:.2f}'
    
    def calcular_desempenho(nota, somatorio):
        desempenho = (nota / somatorio) * 10
        if desempenho <= 2:
            return 'Péssimo'
        elif desempenho <= 4:
            return 'Ruim'
        elif desempenho <= 6:
            return 'Regular'
        elif desempenho < 8:
            return 'Bom'
        else:
            return 'Excelente'

main()