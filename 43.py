peso = float(input('Qual o peso? '))
altura = float(input('Qual a altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso normal. ')
elif 18.5 <= imc < 25:
    print('Peso normal. ')
elif 25 <= imc < 30:
    print('Sobrepeso.')