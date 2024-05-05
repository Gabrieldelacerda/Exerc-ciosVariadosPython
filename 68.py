from random import randint
v = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input("Par ou ímpar? ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total {total}")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você venceu.")
            v += 1
        else:
            print("Perdeu.")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("Você venceu.")
            v += 1
        else:
            print("Você perdeu.")
            break
print(f"Você venceu {v} vezes.")