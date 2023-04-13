import json

# Lê o arquivo JSON
with open('faturamento.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Extrai o vetor de faturamento diário
faturamento = dados['faturamento']

# Calcula o menor valor de faturamento
menor_valor = min(dia['valor'] for dia in faturamento)

# Calcula o maior valor de faturamento
maior_valor = max(dia['valor'] for dia in faturamento)

# Calcula a média mensal de faturamento (ignorando dias sem faturamento)
dias_com_faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias com faturamento diário superior à média mensal
dias_acima_da_media = sum(dia['valor'] > media_mensal for dia in faturamento)

# Imprime os resultados
print('Menor valor de faturamento:', menor_valor)
print('Maior valor de faturamento:', maior_valor)
print('Número de dias com faturamento acima da média mensal:', dias_acima_da_media)