def calcular_fibonacci(numero):
# Gera a sequência de Fibonacci até o número informado.
    fib_sequence = [0, 1]
    
    while True:
        proximo_fib = fib_sequence[-1] + fib_sequence[-2]
        if proximo_fib > numero:
            break
        fib_sequence.append(proximo_fib)
    
    return fib_sequence

def verifica_fibonacci(numero):
# Verifica se o número pertence à sequência de Fibonacci.
    fib_sequence = calcular_fibonacci(numero)
    return numero in fib_sequence

# Número definido no código
# numero_informado = 21  # Por exemplo

# Entrada do usuário
numero_informado = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if verifica_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")