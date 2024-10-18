import json

# Função para calcular o faturamento
def calcular_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    # Filtrar os valores de faturamento, ignorando dias sem faturamento
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

    if not faturamentos:
        return None, None, 0  # Retorna None se não houver faturamento

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)

    # Contar os dias com faturamento superior à média
    dias_acima_media = sum(1 for valor in faturamentos if valor > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

# Importando o arquivo .json e 
arquivo_json = 'Dados.json'  # Nome do arquivo JSON
menor, maior, dias_acima_media = calcular_faturamento(arquivo_json)

print(f'Menor Faturamento: {menor}')
print(f'Maior Faturamento: {maior}')
print(f'Dias com faturamento acima da média: {dias_acima_media}')