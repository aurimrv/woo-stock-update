import pandas as pd

# Carregar os dados dos arquivos CSV fornecidos

# Primeiro arquivo CSV com colunas ID, REF, Stock
file1_path = 'wc-product-export-19-5-2025-1747650616050.csv'
# Segundo arquivo CSV com apenas referências
file2_path = 'estoque-unico.txt'

# Carregar o primeiro arquivo CSV
df1 = pd.read_csv(file1_path)

# Carregar o segundo arquivo (arquivo txt com referências, uma por linha)
with open(file2_path, 'r') as f:
    refs_file2 = f.read().splitlines()

# Obter as referências do primeiro arquivo na coluna 'REF'
refs_file1 = df1['REF'].astype(str).tolist()

# Encontrar referências no segundo arquivo que não estão no primeiro arquivo
refs_not_in_file1 = [ref for ref in refs_file2 if ref not in refs_file1]

print(f'{len(refs_not_in_file1)} referências não cadastradas')
print(refs_not_in_file1)  # Mostrar todas referências faltantes