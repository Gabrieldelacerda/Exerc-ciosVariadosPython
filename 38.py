num = int(input('Digite um número inteiro: '))
print('''Escolha uma conversão:
[1] para binário
[2] para octal
[3] para hexadecimal''')
opcao = int(input('Opção: '))
if opcao == 1:
    print('{} convertido para binario é {}'.format(num, bin(num)))
elif opcao == 2:
    print(f'{num} convertido para octal é {oct(num)}')
else:
    print(f'{num} convertido para hexa é {hex(num)}')