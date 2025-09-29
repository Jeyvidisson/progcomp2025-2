from http.client import FOUND


intNota1 = int(input('Informe a nota da ETAPA 1:'))
intNota2 = int(input('Informe a nota da ETAPA 2:'))

intMedia = round( (intNota1*2 + intNota2*3)/5 )

print(f'Nota da Etapa 1: {intNota1}')
print(f'Nota da Etapa 2: {intNota2}')
print(f'Média: {intMedia}')



#### -> Found <-