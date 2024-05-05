numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Divisão por zero não é permitida."

print(f"Soma: {soma}")
print(f"Subtracao: {subtracao}")
print(f"Multiplicacao: {multiplicacao}")
print(f"Divisao: {divisao}")