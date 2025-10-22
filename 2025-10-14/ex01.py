'''
   Escreva um programa que pede ao usuário para inserir um ano e 
   determina se ele é bissexto ou não. 
   
   Um ano é bissexto se atender a uma das seguintes regras:

      - É divisível por 4, mas não é divisível por 100.

      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
   O programa deve exibir "O ano [ano] é bissexto." ou 
   "O ano [ano] não é bissexto.". 
   
   Use try...except para validar a entrada.
'''

import sys


try:
    ano = int(input("Digite o ano: "));
except ValueError:
    sys.exit(f'ERRO: Deve-se digitar um valor numérico');
except Exception as strERRO:
    sys.exit(f'ERRO: {strERRO}')
else:
    if ano <= 0:
        sys.exit("ERRO: O seu ano tem de ser maior que 0)");

t1 = (ano % 4) 
t2 = (ano % 400)
t3 = (ano % 100)

# ---> print(f' {t1} // {t2} // {t3} //');


if ((t1 == 0) and (t3 != 0)) or (t2 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print('O ano não é bissexto')
