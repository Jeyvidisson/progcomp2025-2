'''
   Desenvolva um programa que calcula o IMC de uma pessoa. 
   
   O programa deve pedir o peso em quilogramas (ex: 70.5) e a 
   altura em metros (ex: 1.75). 
   
   A fórmula do IMC é: peso / (altura * altura). 
   
   Após calcular o IMC, o programa deve exibir o valor e a 
   classificação correspondente, de acordo com a tabela:

      - Abaixo de 18.5: Abaixo do peso
      - 18.5 a 24.9: Peso ideal
      - 25.0 a 29.9: Sobrepeso
      - 30.0 a 34.9: Obesidade Grau I
      - Acima de 35.0: Obesidade Grau II

   O programa deve tratar entradas inválidas (não numéricas) e 
   também verificar se a altura informada é maior que zero para evitar 
   um erro de divisão.      

'''
import sys

try:
    kilos = float(input("Digite o seu peso em kilogramas: "));
    altura = float(input("Digite a sua altura: "));
except ValueError:
    sys.exit(f'ERRO: Deve-se digitar um valor numérico')
except Exception as strERRO:
    sys.exit(f'ERRO: {strERRO}')
else:
    if altura <= 0:
        sys.exit("ERRO: A altura deve ser maior que 0 (ZERO) ")
    if kilos <= 0:
        sys.exit("ERRO: Seu peso deve ser maior que 0 (ZERO) ")
imc = kilos / (altura * altura)

if (imc < 18.5):
    print(f'Abaixo do peso !!! IMC [{imc:.1f}]');
elif (imc >= 18.5) and (imc <= 24.9):
    print(f'Peso Ideal !!! IMC [{imc:.1f}]')
elif (imc >= 25.0) and (imc <= 29.9):
    print(f'Sobrepeso !!! IMC [{imc:.1f}]')
elif (imc >= 30) and (imc <= 34.9):
    print(f' Obesidade Grau I !!! IMC [{imc:.1f}]')
else:
    print(f'Obesidade Grau II !!! IMC [{imc:.1f}]')





#https://github.com/IFRN-ExampleClasses/2025.2-ProgComp/blob/main/2025-09-30%20-%20Condicionais/media_ifrn_frequencia_v2.py