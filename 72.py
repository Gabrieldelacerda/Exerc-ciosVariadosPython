cont = ('zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
        'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente", end=' ')
print(f"Você digitou {cont[num]}")