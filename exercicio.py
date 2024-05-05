casa = float(input('Valor da casa: R$' ))
salario = float(input('Salario do comprador: '))
anos = int(input('Quantos anos de financiamento '))
prestacao = casa / (anos * 12)
print('Para paga uma casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}'.format(casa,anos, prestacao))
minimo = salario * 0.3
if prestacao <= minimo:
    print('Emprestimo autorizado')
else:
    print('Emprestimo negado')