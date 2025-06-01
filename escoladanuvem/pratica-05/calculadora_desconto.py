def calcular_desconto(preco, percentual_desconto):
 desconto = preco * (percentual_desconto/ 100)
 preco_final = preco - desconto
 return preco_final

"""
Crie um programa que receba o preço original de um produto
e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto.
 Requisitos: - Permitir que o usuário informe o preço do produto e o percentual de desconto. - 
 Utilizar operações matemáticas para calcular o valor do desconto e o preço final. - 
 Exibir o preço final com duas casas decimais para garantir precisão. 
 Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

"""

preco_original = float(input("Digite o preço do produto: R$"))
desconto = float(input("Digite o percentual do desconto: "))

preco_desconto = calcular_desconto(preco_original, desconto)

print(f"O preço final com {desconto}% de desconto é: R${preco_desconto: .2f}")
