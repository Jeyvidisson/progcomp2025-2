#Solicite ao usuário uma temperatura em graus Celsius.
#Converta para Fahrenheit.
# F = (C ⋅ 1,8) + 32

print("Conversor de temperatura Celcius para Fahrenheit \n");

valor_celcius = float(input("Digite o valor da temperatura em graus celcius: "));
fahr_temp     = (valor_celcius * 1.8) + 32;
print(f'O valor em Fahrenheit é de: \n{fahr_temp}    ');
