from q2_int_utils import receber_inteiro

def main():
    n = receber_inteiro('Digite um número: ')
    m = receber_inteiro('Digite outro número: ')
    
    def regra_r(n):
        raiz_quadrada = n ** 1.5

        if raiz_quadrada % 7 != 0 and raiz_quadrada % 5 != 0 and raiz_quadrada % 3 != 0 and raiz_quadrada % 2 != 0:
            return True
        else:
            return False
        
    numero = n

    while numero < m:
        if regra_r(numero):
            print(numero)
            

main()