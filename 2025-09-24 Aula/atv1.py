# (1) Desenvolva um programa em Python que solicite ao usuário o valor do raio de um círculo e, 
# em seguida, calcule e exiba a área do círculo. 
# Utilize a fórmula da área do círculo. Considere o valor de π = 3.1416


raio = float(input("Digite o raio do círculo: "));
pi = 3.1416;
area = pi * raio ** 2;

print(f'A área do círculo é: {area:.2f} ');
