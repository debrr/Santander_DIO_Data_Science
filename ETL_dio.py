import pandas as pd
import openai

# ==========================================
# 1. EXTRACT (Extração)
# ==========================================
print("Iniciando Extração...")

# Lendo o CSV completo (conforme a Opção 2 do desafio)
df = pd.read_csv('SDW2023.csv')

# Convertendo para lista de dicionários para simular a resposta da API
users = df.to_dict(orient='records')

# Garantindo que cada usuário tenha o campo 'news' vazio para a transformação
for user in users:
    user['news'] = []

print(f"Extraídos {len(users)} usuários com sucesso.")

# ==========================================
# 2. TRANSFORM (Transformação)
# ==========================================
print("\nIniciando Transformação com IA...")

def generate_ai_news(user):
    # Lógica de fallback (
    nome = user['Nome']
    return f"{nome}, investir é o caminho para multiplicar seu dinheiro. Vamos fortalecer seu futuro!"

for user in users:
    news_content = generate_ai_news(user)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news_content
    })
    print(f"Mensagem gerada para {user['Nome']}: {news_content}")

# ==========================================
# 3. LOAD (Carregamento)
# ==========================================
print("\nIniciando Carregamento (Load)...")

df_final = pd.DataFrame(users)
df_final.to_csv('SDW2023_finalizado.csv', index=False)

print("Sucesso! O arquivo 'SDW2023_finalizado.csv' foi gerado com as mensagens personalizadas.")