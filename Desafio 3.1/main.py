import xml.etree.ElementTree as ET

def calcular_faturamento(dados_faturamento):
# Calcula o menor e maior faturamento, além dos dias acima da méa.
    faturamentos = []

    for dia in dados_faturamento:
        valor = dia.text
        if valor != "null": 
            faturamentos.append(float(valor))

    if not faturamentos:
        return None, None, 0

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, media_faturamento, dias_acima_media

# Leitura dos dados
def ler_dados_xml(arquivo):
    tree = ET.parse(arquivo)
    root = tree.getroot()
    return root.findall('dia')

# Exemplo de dados
arquivo_xml = 'Desafio 3.1/faturamento.xml' 
dados = ler_dados_xml(arquivo_xml)

menor, maior, media, dias_acima = calcular_faturamento(dados)

# Resultados
if menor is not None:
    print(f"Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Média de faturamento: {media:.2f}")
    print(f"Número de dias acima da média: {dias_acima}")
else:
    print("Não há dados de faturamento válidos.")
