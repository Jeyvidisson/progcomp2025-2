#Peça ao usuário um valor em reais (R$) e a cotação do dólar.
#Calcule e exiba quantos dólares ele teria com esse valor.
print("Conversor de moeda:                         ");
valor_   = float(input("Digite o valor em reais: "  ));
cotacao_ = float(input("Digite a cotação do dólar: "));

conv_    = valor_ * cotacao_;
print(f'Você teria [ {conv_} ] Dólares');

 