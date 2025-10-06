# Solicita ao usuário que digite a coordenada X e armazena o valor.
# A função input() lê o que o usuário digita como texto (string).
# A função float() converte esse texto para um número decimal (ponto flutuante),
# permitindo que usemos valores como 2.5, -3.0, etc.
fltCoordX = float(input('Digite a coordenada X: '))

# Faz o mesmo para a coordenada Y, solicitando o valor e convertendo para float.
fltCoordY = float(input('Digite a coordenada Y: '))

# Início da estrutura de decisão para verificar a localização do ponto.
# O programa vai testar cada condição (if/elif) em ordem, e a primeira
# que for verdadeira será executada.

# Verifica se o ponto está no 1º Quadrante.
# A condição (fltCoordX > 0) and (fltCoordY > 0) só é verdadeira se
# AMBAS as coordenadas forem positivas.
if (fltCoordX > 0) and (fltCoordY > 0):
   print('O ponto está no 1º Quadrante.')

# Se a primeira condição for falsa, esta será testada.
# Verifica se o ponto está no 2º Quadrante.
# A condição é verdadeira se X for negativo E Y for positivo.
elif (fltCoordX < 0) and (fltCoordY > 0):
   print('O ponto está no 2º Quadrante.') 

# Se as anteriores forem falsas, esta será testada.
# Verifica se o ponto está no 3º Quadrante.
# A condição é verdadeira se AMBAS as coordenadas forem negativas.
elif (fltCoordX < 0) and (fltCoordY < 0):
   print('O ponto está no 3º Quadrante.')

# Se as anteriores forem falsas, esta será testada.
# Verifica se o ponto está no 4º Quadrante.
# A condição é verdadeira se X for positivo E Y for negativo.
elif (fltCoordX > 0) and (fltCoordY < 0):
   print('O ponto está no 4º Quadrante.')

# Se as anteriores forem falsas, esta será testada.
# Verifica se o ponto está exatamente na origem do plano cartesiano.
# A condição é verdadeira se AMBAS as coordenadas forem iguais a zero.
elif (fltCoordX == 0) and (fltCoordY == 0):
   print('O ponto está na origem (0,0).')

# Se as anteriores forem falsas, esta será testada.
# Verifica se o ponto está sobre o eixo X.
# Isso acontece quando a coordenada Y é zero, e a X não é (casos em que X
# também é zero já foi tratado na condição da origem).
elif (fltCoordY == 0):
   print('O ponto está sobre o eixo X.')

# Se NENHUMA das condições anteriores (if/elif) for verdadeira,
# o programa executa o que está no "else".
# Neste ponto, a única possibilidade que sobrou é o ponto estar sobre o eixo Y
# (ou seja, quando a coordenada X é zero e a Y não é).
else:
   print('O ponto está sobre o eixo Y.')