"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação. """

import requests
from datetime import datetime

def conversor_moedas(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        Moeda: {moeda} para BRL
        Valor atual: R$ {float(cotacao["bid"]):.2f}
        Máxima: R$ {float(cotacao["high"]):.2f}
        Mínima: R$ {float(cotacao["low"]):.2f}
        Data e Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
        """
    except requests.RequestException as e:
        return f"Erro ao obter a cotação {e}"
    

moeda = input("Digite o código da moeda para cotação (ex. USD, EUR, GBP): ").upper()
print("\nObtendo a cotação...")
resultado = conversor_moedas(moeda)
print(resultado)