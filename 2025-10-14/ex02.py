'''
   Desenvolva um código em Python que solicite ao usuário que informe os 
   comprimentos dos três lados de um triângulo. 
   
   Em seguida, verifique se esses comprimentos podem formar um triângulo. 
   Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e 
   classifique-o quanto aos lados e aos ângulos.

   Instruções:
      - Peça ao usuário para inserir os comprimentos dos três lados do triângulo;
      - Verifique se os comprimentos fornecidos podem formar um triângulo. 
        Caso contrário, informe que não é possível formar um triângulo com esses lados;
      - Se for possível formar um triângulo, calcule os três ângulos do triângulo;
      - Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) 
        e aos ângulos (agudo, obtuso ou retângulo);
      - Exiba a classificação do triângulo quanto aos lados e aos ângulos.

   Observações:
      - Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, 
        é necessário verificar a seguinte condição: A soma de quaisquer dois lados de 
        um triângulo deve ser sempre maior que o terceiro lado;
      - Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
      - Para classificar quanto aos lados, verifique se os três lados são iguais 
        (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são 
        diferentes (escaleno);
      - Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 
        90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) 
        ou se todos os ângulos são menores que 90 graus (agudo);
      - Considere que os ângulos são expressos em graus.

   Dica: Utilize a biblioteca math.
   https://docs.python.org/3/library/math.html
'''









from cmath import cos
import sys
import os
import math





try:
    Lado_A = int(input('Digite o valor do primeiro lado: '));
    Lado_B = int(input('Digite o valor do segundo lado: '));
    Lado_C = int(input('Digite o valor do terceiro lado: '));
except ValueError:
    sys.exit(f'ERRO: Deve-se digitar um valor numérico');
except Exception as strERRO:
    sys.exit(f'ERRO: {strERRO}');

if (Lado_A + Lado_B > Lado_C) and (Lado_B + Lado_C > Lado_A) and (Lado_A + Lado_C > Lado_B):
    print('É um triângulo !!!');
else:
    sys.exit('Não é um triângulo');

Angulo_A = Lado_B**2 + Lado_C**2 - 2*Lado_B*Lado_C * cos(Lado_A)
Angulo_B = Lado_A**2 + Lado_C**2 - 2*Lado_A*Lado_C * cos(Lado_B)
Angulo_C = Lado_A**2 + Lado_B**2 - 2*Lado_A*Lado_B * cos(Lado_C)

