def contar_palavras(frase):
    palavras = frase.split()
    numero_palavras = len(palavras)
    return numero_palavras

def inverter_ordem_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = palavras[::-1]
    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase

frase = input('Digite uma frase:')

numero_palavras = contar_palavras(frase)
print(f"A frase possui {numero_palavras} palavras.")

frase_invertida = inverter_ordem_palavras(frase)
print("Frase com as palavras invertidas:", frase_invertida)