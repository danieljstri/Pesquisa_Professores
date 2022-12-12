import pandas as pd

# Lê uma base dados Excel com o nome de todos os professores e suas respectivas áreas
tabela1 = pd.read_excel('prof-data-2.xlsx', engine='openpyxl')

# Armazena as colunas "AREA1" e "AREA2" em variáveis
column1 = tabela1['AREA1']
column2 = tabela1['AREA2']

# Listas (arrays) do nome dos professores
areas1_list = []
areas2_list = []

# Dicionários finais
data_area1 = {}
data_area2 = {}

# Adiciona o nome de todas as áreas em uma lista (array) [Primeira área]
for item1 in column1:
    if item1 in areas1_list:
        pass
    else:
        areas1_list.append(item1)

# Adiciona o nome de todas as áreas em uma lista (array) [Segunda área]
for item2 in column2:
    if item2 in areas2_list:
        pass
    else:
        areas2_list.append(item2)

# Loop que vai organizar todos os professores por área
# Lê a lista com os nomes das áreas
for item in areas1_list:
    # Nessa parte, ele irá filtrar na tabela original todas as linhas em que a "AREA1" for
    # igual ao respectivo item da lista e vai gerar uma tabela filtrada. Por exemplo: Todas
    # as linhas em que "AREA1" for "Engenharia de Software"
    filtroNome = tabela1.loc[tabela1["AREA1"] == f"{item}"]
    lista_nomes = []
    # Nessa parte, ele irá pegar o nome de todos os professores da tabela filtrada e adicionar
    # em uma lista
    for items in filtroNome['NOME']:
        lista_nomes.append(items)
    # Agora ele adiciona no dicionário a chave (key) sendo o nome da área e o item sendo a lista
    # com o nome dos professores
    data_area1[item] = lista_nomes

# Mesma função do loop anterior
for item in areas2_list:
    filtroNome = tabela1.loc[tabela1["AREA2"] == f"{item}"]
    lista_nomes = []
    for items in filtroNome['NOME']:
        lista_nomes.append(items)
    data_area2[item] = lista_nomes

# Print dos resultados
print(data_area1)
print('-'*15)
print(data_area2)