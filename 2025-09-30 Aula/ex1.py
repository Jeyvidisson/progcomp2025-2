'''
   Faça um programa para calcular média e a frequência de uma disciplina 
   no IFRN.

   Sabe-se que são duas notas e que o peso da primeira nota é 2
   e o peso da segunda nota é 3 e que as notas são compreendidas entre
   0 e 100.

   Caso as notas não sejam válidas, deve-se informar ao usuário e sair do 
   programa.

   Sabe-se também que para se calcular a frequência, deve-se informar a carga 
   horária da disciplina (em horas/aula) e a quantidade de faltas do aluno.

   - Teste 1: Nota1 = 50 e Nota2 = 65
   - Teste 2: Nota1 = 73 e Nota2 = 19
   - Teste 3: Nota1 = 72 e Nota2 = 29
   - Teste 4: Nota1 = 10 e Nota2 = 21

# Mostrando se o aluno está APROVADO, PROVA FINAL ou REPROVADO
# todo: implementar a lógica para mostrar se o aluno foi 
# reprovado por nota, por frequência ou por ambos

'''

from statistics import median
import sys

print('Calculadora de média ponderada disciplina; ');

nota_01 = int(input("Digite a primeira nota:  "));

if not (nota_01 >= 0) and (nota_01 <= 100):
    sys.exit('Primeira nota é inválida !!!')

nota_02 = int(input("Digite a segunda nota:   "));

if not (nota_02 >= 0) and (nota_02 <= 100):
    sys.exit('Segunda nota é inválida !!!')

peso_01 = 2;
peso_02 = 3;

mp = ((nota_01 * peso_01) + (nota_02 * peso_02)) / (peso_01 + peso_02);

Carga_horaria = int(input("Digite a carga horária da disciplina (Horas/Aula):  "));
Faltas = int(input("Informe a quantidade de faltas do aluno:  "));

Frequencia = round((1 - (Faltas / Carga_horaria)) * 100), 1

print(f'Total de Aulas [ {Carga_horaria} ]');

# Validar se a carga horária é maior que zero e menor ou igual a 360

if not (0 < Carga_horaria <= 360):
   sys.exit('Carga Horária inválida! Deve ser entre 1 e 360 horas/aula.')

if not (0 <= Faltas <= Carga_horaria):
   sys.exit(f'Quantidade de Faltas inválida! Deve ser entre 1 e {Carga_horaria} horas/aula.')

print(f'Total de Faltas [ {Faltas} ]');
print(f'Frequência [ {Frequencia} ]')
print(f'A sua média da disciplina correspondente é de: {mp}');

if (mp >= 60) and (Frequencia >= 75):
    print("Você foi aprovado");
elif (mp >= 20) and (Frequencia >= 75):
    print("Você está em prova final");
else:
    print("Você foi reprovado");
if (mp < 20) and (Frequencia < 75):
    print('Motivo: Reprovado por falta e frequência');

elif (mp < 20):
    print('Reprovado por nota')
else:
    print('Reprovado por falta')
