
from q2_int_utils import *

def main():
    n = receber_inteiro('Digite um número: ')
    m = receber_inteiro('Digite outro número: ')
    
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
        
    for i in range(n, m+1):
        if eh_primo(i):
            print(i)
            

main()