listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        else:
            menor = listanum[c]

print(f"Maior: {maior} e Menor: {menor}")