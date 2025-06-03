"""
PRATICA 07 - ATIVIDADE 03
Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de
pessoas, com colunas Nome, Idade e Cidade."""

import csv
def ler_csv(nome_arquivo):
    try:
        with open (nome_arquivo, 'r', newline='') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ")
    ler_csv(nome_arquivo)
