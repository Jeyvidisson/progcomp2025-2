'''
   Crie um programa que calcula o salário semanal de um funcionário.
   
   O programa deve solicitar o número de horas trabalhadas na semana e o 
   valor que ele recebe por hora. A jornada de trabalho padrão é de 40 horas 
   semanais. Horas trabalhadas acima de 40 devem ser pagas com um adicional 
   de 50% (o valor da hora extra é 1.5 vezes o valor da hora normal). 
   
   O programa deve exibir o salário total. 
   
   Garanta que o programa trate o caso de o usuário digitar valores não 
   numéricos.

'''
import sys
from winreg import SaveKey

try:
    horas_trabalhadas = int(input("Digite as suas horas trabalhadas: "));
    sal_hora          = float(input("Digite o seu salário por hora: "   ));
except ValueError:
    sys.exit('ERRO: Informe apenas números inteiros...');
except Exception as strErro:
    sys.exit('ERRO: Você deve digitar um valor numérico !!!');
else:
    if horas_trabalhadas < 0:
        sys.exit('ERRO: O número de horas não pode ser negativo !!!');
    if sal_hora < 0:
        sys.exit('ERRO: O valor da hora não pode ser negativo !!!');

if horas_trabalhadas > 40:
    horas_extras = horas_trabalhadas - 40
    horas_trabalhadas = 40
    salario = (horas_trabalhadas * sal_hora) + ( horas_extras * horas_trabalhadas * 1.5);
    print(f'Você trabalhou {horas_trabalhadas + horas_extras} horas nesta semana.');
    print(f'O valor da hora é de R${horas_trabalhadas:.2f}');
    print(f'Seu salário semanal é de R${salario:.2f}');
    print(f'Seu salário é de R${salario * 4:.2f}');