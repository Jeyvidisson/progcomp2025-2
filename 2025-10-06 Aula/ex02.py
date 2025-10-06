from ast import Div
from logging import exception
import sys
try:
    Dividendo = int(input('Informe o primeiro número inteiro:'   ));
    Divisor   = int(input('Informe o segundo número inteiro:'    ));
    Divisao = Dividendo / Divisor

except ZeroDivisionError as zeroerror:
    sys.exit(f'Exceção: {sys.exc_info()[0]} -> {zeroerror} A divisão não pode ser zero')
except ValueError:
    sys.exit(f'Erro informe apenas números inteiros')
except Exception as strError:
    sys.exit(f'Exceção: {sys.exc_info()[0]} -> {strError}')
else:
    print(f'{Dividendo} / {Divisor} = {Divisao} = {Divisao}');

