"""
Crie uma função que calcule a gorjeta a ser deixada em
um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna:
float: O valor da gorjeta calculada
"""
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

total_conta = float(input('Insira o valor total da conta: R$ ' ))
porcentagem = float(input('Insira a porcentagem da gorjeta (%): '))

gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f'Para uma conta no total de R${total_conta:.2f}, a gorjeta de {porcentagem}% é R${gorjeta:.2f}')