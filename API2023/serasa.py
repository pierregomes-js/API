def main():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    sc1 = (a * 2.6) + (b * 5.7) + (c * 1.7)
    sc2 = (a * 6.2) + (b * 1.9) + (c * 1.9)

    faixa_1 = faixa_antiga(sc1)
    faixa_2 = faixa_nova(sc2)



    print(f'Score 1.0 : {sc1} - {faixa_1}')
    print(f'Score 2.0 : {sc2} - {faixa_2}')

def faixa_antiga(score):
    if score < 400:
        return 'Baixo'
    elif score < 600:
        return 'Regular'
    elif score < 800:
        return 'Bom'
    else:
        return 'Muito bom'

def faixa_nova(score):
    if score <= 300:
        return 'Baixo'
    elif score <= 500:
        return 'Regular'
    elif score <= 700:
        return 'Bom'
    else:
        return 'Muito bom'

main()