"""
Crie um programa que gera uma senha aleatória com o módulo random,
utilizando caracteres especiais, possibilitando o usuário 
a informar a quantidade de caracteres dessa senha aleatória.

string.ascii_letters: letras maiúsculas e minúsculas.
string.digits: números de 0 a 9.
string.punctuation: caracteres especiais como !@#$%&*(), etc.
random.choice(): escolhe aleatoriamente um caractere da lista.1
"""

import random
import string

def gerar_senha(tamanho):
    # Define os caracteres que podem ser usados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Solicita ao usuário o tamanho da senha
try:
    tamanho = int(input("Informe a quantidade de caracteres da senha: "))
    if tamanho <= 0:
        print("Por favor, digite um número maior que zero.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print(f"Sua senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, digite um número válido.")