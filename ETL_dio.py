import pandas as pd
import json

# ==========================================
# 1. EXTRACT (Extração)
# ==========================================
print("Iniciando Extração...")

# Lendo o CSV (Certifique-se que o arquivo existe na pasta)
try:
    df = pd.read_csv('Lista_dio.csv')
    # Convertendo para lista de dicionários (Opção 2 do desafio)
    users = df.to_dict(orient='records')
    
    for user in users:
        user['news'] = [] # Preparando o campo que a API usaria
    
    print(f" Extraídos {len(users)} usuários com sucesso.")
except FileNotFoundError:
    print(" Erro: Arquivo Lista_dio.csv não encontrado!")
    users = []

# ==========================================
# 2. TRANSFORM (Transformação)
# ==========================================
if users:
    print("\nIniciando Transformação...")

    def generate_ai_news(user):
        # Usando .get() para evitar erro caso a coluna mude de 'Nome' para 'name'
        nome = user.get('Nome', user.get('name', 'Cliente'))
        return f"{nome}, investir é o caminho para multiplicar seu dinheiro. Vamos fortalecer seu futuro!"

    for user in users:
        news_content = generate_ai_news(user)
        user['news'].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news_content
        })
        print(f"  - Mensagem gerada para: {user.get('Nome', 'Usuário')}")

# ==========================================
# 3. LOAD (Carregamento)
# ==========================================
if users:
    print("\nIniciando Carregamento (Load)...")

    # Salvando o resultado em um novo CSV
    df_final = pd.DataFrame(users)
    df_final.to_csv('Lista_dio_finalizado.csv', index=False)

    # Exibindo o JSON final no console para conferência (estilo a resposta da API)
    print("\n--- Resultado Final (Simulação API) ---")
    print(json.dumps(users, indent=2, ensure_ascii=False))
    
    print("\nSucesso! O arquivo 'SDW2023_finalizado.csv' foi gerado.")