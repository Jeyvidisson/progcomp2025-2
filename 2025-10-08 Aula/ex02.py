
'''

   Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

   Exemplo: 2456 = 17 (2 + 4 + 5 + 6)

   DICA: Vocês irão usar o operador de divisão inteira (//) e o operador de resto de divisão inteiro (%)

'''



## 242

#inteiro positivo

number = int(input("Digite um número positivo e de 4 digitos"));
t1 = number // 1000
p1 = number % 1000

t2 = p1 // 100
p2 = number % 100

t3 = p2 // 10
p3 = number % 10

t4 = p3 // 1
p4 = number % 1

soma = t1 + t2 + t3 + t4





 
print(f' {t1} {t2} {t3} {t4} a soma é: {soma}')

#[ {t2}, {p2} ] [ {t3}, {p3} ] [ {t4}, {p4} ]'


