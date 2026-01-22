# Pipeline ETL com Python: Santander 2025 - Ciência de Dados com Python 

Este projeto faz parte do desafio da **Santander 2025 - Ciência de Dados com Python**. O objetivo é demonstrar o fluxo de **ETL (Extração, Transformação e Carregamento)** aplicado a um cenário bancário, onde simulamos a geração de mensagens personalizadas de investimento para clientes.

## Entendendo o Desafio
O foco principal foi entender como os dados fluem. Como a API original pode estar indisponível, utilizei a **Alternativa 2** sugerida no desafio: processamento via arquivo CSV. 

## Tecnologias Utilizadas
* **Linguagem:** Python 3.14+
* **Biblioteca:** Pandas (para manipulação de dados)
* **Formato de saída:** JSON e CSV

## O Fluxo ETL

### 1. Extract (Extração)
O script lê um arquivo chamado `Lista_dio.csv`. Este arquivo contém os dados básicos dos clientes (Nome, Conta, Cartão). Os dados são convertidos em uma lista de dicionários para facilitar a manipulação.

### 2. Transform (Transformação)
Nesta etapa, criamos uma lógica para gerar mensagens personalizadas. 
- **Regra de Negócio:** Para cada cliente, o script gera uma frase incentivando investimentos para fortalecer o futuro financeiro.
- **Segurança:** Utilizei o método `.get()` para garantir que o código funcione mesmo se o nome da coluna no CSV variar entre 'Nome' ou 'name'.

### 3. Load (Carregamento)
Os dados transformados são exportados de volta para dois formatos:
- Um novo arquivo CSV: `Lista_dio_finalizado.csv`.
- Uma exibição em formato JSON no terminal, simulando a resposta que uma API entregaria.

---
**Projeto desenvolvido por Débora** *Estagiária em Dados | Estudante de Ciência de Dados*
