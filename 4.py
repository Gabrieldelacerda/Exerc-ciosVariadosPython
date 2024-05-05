def verificar_numero(numero):
    if numero > 0:
        print("Número positivo.")
    elif numero < 0:
        print("Número negativo.")
    else:
        print("O número é zero.")

while True:
    numero = float(input("Digite um número (ou zero para sair): "))

    if numero == 0:
        print("Finalizando...")
        break

    verificar_numero(numero)