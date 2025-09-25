#Peça ao usuário o valor da conta e a porcentagem de gorjeta que deseja dar.
#Calcule o valor total a pagar e exiba com uma mensagem.

conta = float(input("Digite o valor da conta: "));
gorj =  float(input("Digite a porcentagem da gorjeta: "));

resultado = conta * (gorj / 100) ;
print(f'Você deve pagar \n[ { resultado } ] ');
