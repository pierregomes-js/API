from q4_text_utils import *
from q2_int_utils import *

def main():
    somatorio = 0
    nome_animal = receber_texto_min('Digite um nome de um animal(mínimo: 7 letras): ', 7)
    num = receber_inteiro(f'Digite a quantidade de dígitos de {nome_animal}: ')
    contador = 1
    somatorio += num

    def eh_primo(n):
        if n < 2:
            return False
        regra_r = n ** 0.5
        divisores = 2

        while divisores <= regra_r:
            if n % divisores == 0:
                return False
            divisores += 1

        return True
    
    while not (eh_primo(num)):
        somatorio += num

        nome_animal = receber_texto_min('Digite um nome de um animal(mínimo: 7 letras): ', 7)
        num = receber_inteiro(f'Digite a quantidade de dígitos de {nome_animal}: ')
        contador += 1

    media = somatorio / contador

    print(f'Somatório dos números digitados: {somatorio}')
    print(f'Média dos números digitados: {media}')
    

main()