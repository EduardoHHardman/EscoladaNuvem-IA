"""
Crie um programa que gera um perfil de usuário aleatório usando
a API 'Random User Generator'. O programa deve exibir o nome, 
email e país do usuário gerado.
"""
import requests

def gerar_usuario():
    url = 'https://randomuser.me/api/'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Gera exceção se status != 200
        dados = response.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        return nome, email, pais
    
    except requests.RequestException as e:
        return f"Erro ao acessar a API: {e}"
    
print("Gerando um usuario aleatorio...")
usuario = gerar_usuario()
print(usuario)
