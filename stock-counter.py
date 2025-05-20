from collections import Counter
import csv

# Ler o arquivo de texto
with open('estoque-ordenado.txt', 'r') as file:
    codigos = [linha.strip() for linha in file if linha.strip()]

# Contar as ocorrências de cada código
contagem = Counter(codigos)

# Gerar o arquivo CSV
with open('estoque_contagem.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['REF', 'Stock'])  # Cabeçalho
    for codigo, quantidade in contagem.items():
        writer.writerow([codigo, quantidade])

