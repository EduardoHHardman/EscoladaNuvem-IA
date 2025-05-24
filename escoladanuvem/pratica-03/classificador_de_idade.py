# Classificador de idade do usuário


# Captura a idade do usuário
idade = int(input("Digite a sua idade: "))

#Verificação de idade
if idade >= 0 and idade <= 12:
    print("Você é criança.")

elif idade >= 13 and idade <= 17:
    print("Você é adolescente")

elif idade >= 18 and idade <= 59:
    print("Você é Adulto")

else:
   print("Você é idoso.")