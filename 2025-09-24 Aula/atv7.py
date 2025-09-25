#Peça ao usuário a distância percorrida (em km) e o tempo gasto (em horas).
#Calcule a velocidade média e exiba o resultado.
# Vm = deltaS / deltaT
print('Calculadora de velocidade media \n');

valor_dist = float(input("Digite o valor da distancia percorrida em km: "));
valor_temp = float(input("Digite o valor do tempo gasto em horas: "));

velocidade_media = valor_dist / valor_temp;
print(f'A sua velocidade média é de: \n[ {velocidade_media:.2f}km/h ]  ');
