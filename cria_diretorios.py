import os
import pandas as pd

# Lê a base de dados com os dados dos professores
tabela1 = pd.read_excel('prof-data-2.xlsx', engine='openpyxl')

# Armazena a coluna "NOME" em uma variável
coluna_nomes = tabela1['NOME']

# Loop para ler cada item da coluna nome e criar os diretórios com os nomes de cada professor
for item in coluna_nomes:
    # Formata o nome do professor para: "Daniel_José_Silva_Trindade
    nome = item.split()
    nome1 = '_'.join(nome)
    # Verifica se o diretório existe, se não, ele cria o diretório com o nome do professor formatado
    # e duas pastas de pesquisa
    if not os.path.exists(f'D:\Programação\Root\Pesquisas_Professores\{nome1}\Pesquisa1'):
        os.makedirs(f'D:\Programação\Root\Pesquisas_Professores\{nome1}\Pesquisa1')
    if not os.path.exists(f'D:\Programação\Root\Pesquisas_Professores\{nome1}\Pesquisa2'):
        os.makedirs(f'D:\Programação\Root\Pesquisas_Professores\{nome1}\Pesquisa2')
    print(f'Pasta do professor {item} foi criada.')