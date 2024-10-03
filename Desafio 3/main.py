import json

def calcular_faturamento(dados_faturamento):
# Calcula o menor e maior faturamento, além dos dias acima da média.
    faturamentos = [valor for valor in dados_faturamento.values() if valor is not None]

    if not faturamentos:
        return None, None, 0

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, media_faturamento, dias_acima_media

# Leitura da base de dados
def ler_dados_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

# Exemplo de dadis
arquivo_json = 'Desafio 3/faturamento.json'  
dados = ler_dados_json(arquivo_json)

menor, maior, media, dias_acima = calcular_faturamento(dados['faturamento'])

# Resultado
if menor is not None:
    print(f"Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Média de faturamento: {media:.2f}")
    print(f"Número de dias acima da média: {dias_acima}")
else:
    print("Não há dados de faturamento válidos.")