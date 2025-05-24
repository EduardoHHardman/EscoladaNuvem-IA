# Cálculo do Índice de Massa Corporal (IMC) de uma pessoa

# Captura o peso do do usuário
peso = float(input("Digite o seu peso (em Kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso.")
    
elif imc >= 18.5 and imc < 25:
    print("Classificação: Peso normal.")

elif imc >= 25 and imc < 30:
    print("Classificação: Sobrepeso.")

else:
    print("Classificação: Obeso")
