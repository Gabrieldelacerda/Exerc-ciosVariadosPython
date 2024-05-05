soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c

print(f'A soma dos valores é {soma} e tem {cont} valores.')
