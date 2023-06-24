# Aula 15 – Interrompendo repetições while

# Comando "break" 

cont = 1

while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

# Usando flags '999'

n = 0

while n != 999:
    n = int(input('Digite um núemro: '))

# Exemplo onde o flag '999' é somado junto

n = s = 0

while True:
    n = int(input('Digite um núemro: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

# # Exemplo de f's strings

print(f'A soma vale {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome , idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2


nome = 'José'
idade = 33
salário = 987.3

print(f'O {nome:-^20} tem {idade} anos e ganha {salário:.2f}.')