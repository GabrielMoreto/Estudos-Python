# Aula 7: Operadores Aritméticos
# + : Adição
5 + 2 == 7
# - : Subtração
5 - 2 == 3
# * : Multiplicação
5 * 2 == 10
# / : Divisão
5 / 2 == 2.5
# ** : Potência
5 ** 2 == 25
# // : Divisão Inteira
5 // 2 == 2
# % : Resto da Divisão
5 % 2 == 1

# Ordem de Precedência
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

# Exemplo de Ordens de Precedência:
n1 = 5 + 3 * 2
print(n1)

n2 = 3 * 5 + 4 ** 2
print(n2)

n3 = 3 * ( 5 + 4 ) ** 2
print(n3)

# Prática:
# Raiz quadrada;
n1 = 25**(1/2)
n1 = 81**(1/2)
print(n1)

# # Raiz cúbica;
n1 = 127**(1/3)
print(n1)

# Strings;
n1 = 'Oi' + 'Olá'
print(n1)

n1 = 'Oi' * 5
print(n1)

n1 = '=' * 20
print(n1)

# Para deixar o nome com 20 caracteres
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))

# Para deixar o nome com 20 caracteres e alinhar a direita
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))

# Para deixar o nome com 20 caracteres e alinhar a esquerda
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))

# Para deixar o nome com 20 caracteres e centralizar
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))

# Para deixar o nome com 20 caracteres centralizar e adiconar = para preencher
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

# Prática:
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# Utilizar \n para quebrar a linha e end = '' para não quebrar de um print para o outro
print('A soma é {}, \n o produto é {}, e a \n divisão {:.3f}'.format(s, m, d), end = ' ')
print('Divisão inteira {} e potência {}'.format(di, e))