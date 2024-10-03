# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# String definida no código
string_original = "Target Sistemas"

# Entrada do usuário
# string_original = input("Informe uma string: ")

resultado = inverter_string(string_original)

# Resultado
print(f"String original: {string_original}")
print(f"String invertida: {resultado}")
