# Faturamento por estado
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Faturamento total
faturamento_total = sum(faturamento_por_estado.values())

# Percentual de representação de cada estado
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_por_estado.items()}

# Resultados
print("Percentual de faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")