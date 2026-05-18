import pandas as pd

# Lê o arquivo CSV criado na mesma pasta do script
dados = pd.read_csv("academia.csv")

# Exibe o conteúdo completo da tabela no terminal
print(dados)
# ==========================================
# ATIVIDADE 5 — Média de Desempenho
# ==========================================
print("--- ATIVIDADE 5 ---")

# Executa o cálculo da média de horas de treino
media_horas_treino = dados["Horas_Treino"].mean()

print(f"A média da coluna Horas_Treino é: {media_horas_treino:.2f} horas")
print("\n" + "=" * 50 + "\n")