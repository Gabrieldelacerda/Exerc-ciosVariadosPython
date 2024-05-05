from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for numero in n:
    print(numero, end=' ')
print(f"\nO maior valor é {max(n)}")
print(f"O menor valor é {min(n)}")