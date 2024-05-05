def verifica_fibonacci(numero):
    fib = [0, 1]
    while fib[-1] < numero:
        fib.append(fib[-1] + fib[-2])
    if numero in fib:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(verifica_fibonacci(numero))
