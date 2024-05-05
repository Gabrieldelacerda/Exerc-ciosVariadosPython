with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Hello World")
    arquivo.write("Arquivo em Python.")
    arquivo.write("Algumas linhas de texto.")

with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)