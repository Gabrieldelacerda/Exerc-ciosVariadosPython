from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('Você deve se alistar.')
elif idade <18:
    print('Ainda não chegou sua hora.')
elif idade >18:
    print('Você deveria ter se alistado em {} anos pra trás.'.format(idade-18))