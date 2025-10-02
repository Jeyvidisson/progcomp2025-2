'''
   Fazer um programa que solicite ao usuário dois números. Esses números
   correspondem as coordenadas x e y de um ponto em um plano cartesiano.

   Após receber os números, o programa deve informar em qual quadrante
   o ponto se encontra. 

   Lembrete: O plano cartesiano é dividido em quatro quadrantes:
   - Quadrante 1: Ambas as coordenadas (x e y) são positivas;
   - Quadrante 2: A coordenada x é negativa e a coordenada y é positiva;
   - Quadrante 3: Ambas as coordenadas (x e y) são negativas;
   - Quadrante 4: A coordenada x é positiva e a coordenada y é negativa;
   - Se o ponto estiver sobre um dos eixos (x ou y), o programa deve informar
     que o ponto está sobre o eixo correspondente:
       - Sobre o eixo x: y = 0
       - Sobre o eixo y: x = 0
   - Se o ponto for a origem (0,0), o programa deve informar que o ponto está 
     na origem.

'''


x = float(input("Digite o número [ x ] do plano cartesiano: "));
y = float(input("Digite o número [ y ] do plano cartesiano: "));

if (x > 0) and ( y > 0):
    print(f'O ponto: ({x} , {y}) se encontra no primeiro quadrante ');
elif (x < 0) and (y > 0):
    print(f'O ponto: ({x} , {y}) se encontra no segundo quadrante  ');
elif (x < 0) and (y < 0):
    print(f'O ponto: ({x} , {y}) se encontra no terceiro quadrante ');
elif (x > 0) and (y < 0):
    print(f'O ponto: ({x} , {y}) se encontra no quarto quadrante   ');
elif (x == 0) and (y == 0):
    print('O ponto está na origem');
elif (x == 0) or (y == 0):
    if (x == 0):
        print(f'Sobre o eixo X: x = 0');
    elif (y == 0):
        print(f'Sobre o eixo Y: y = 0');
