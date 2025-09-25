# (2) 02 - Desenvolva um programa em Python que solicite ao usuário os valores da base maior, 
# base menor e altura de um trapézio e, em seguida, calcule e exiba a sua área. 
# Utilize a fórmula da área do trapézio.


base_maior = int(input("Digite a base maior: "));
base_menor = int(input("Digite a base menor: "));
altura_    = int(input("Digite a altura do trapézio"));
area       = ((base_maior + base_menor) * altura_) / 2

print(f'A área do seu trapézio é de: {area}');