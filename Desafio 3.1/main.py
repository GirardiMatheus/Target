import xml.etree.ElementTree as ET

def calcular_faturamento(dados_faturamento):
#  Calcula o menor e maior faturamento, além dos dias acima da média.
    faturamentos = [float(row.find('valor').text) for row in dados_faturamento if float(row.find('valor').text) > 0]

    if not faturamentos:
        return None, None, 0

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, media_faturamento, dias_acima_media

def ler_dados_xml(arquivo):
    tree = ET.parse(arquivo)
    root = tree.getroot()
    return root.findall('row')

# Dados
arquivo_xml = 'Desafio 3.1/faturamento.xml'  
dados = ler_dados_xml(arquivo_xml)

menor, maior, media, dias_acima = calcular_faturamento(dados)

if menor is not None:
    print(f"Menor faturamento: {menor:.2f}")
    print(f"Maior faturamento: {maior:.2f}")
    print(f"Média de faturamento: {media:.2f}")
    print(f"Número de dias acima da média: {dias_acima}")
else:
    print("Não há dados de faturamento válidos.")