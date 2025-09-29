'''
   Faça um programa para calcular média de uma disciplina no IFRN,
   sabendo que são duas notas e que o peso da primeira nota é 2
   e o peso da segunda nota é 3.
'''

print('Calculadora de média ponderada disciplina; ');

nota_01 = int(input("Digite a primeira nota:  "));
nota_02 = int(input("Digite a segunda nota:   "));
peso_01 = 2;
peso_02 = 3;

mp = ((nota_01 * peso_01) + (nota_02 * peso_02)) / (peso_01 + peso_02);

if (mp >= 60):
    print("Você foi aprovado");
elif (mp >= 20):
    print("Você está em prova final");
else:
    print("Você foi reprovado");

print(f'A sua média da disciplina correspondente é de: {mp}');
