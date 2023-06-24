# # print e input são funçôes, para escrever uma string utilizar sempre aspas simples ''
# # todo conteúdo dentro de aspas simples é considerado texto

# # Exemplo string
print('Olá, Mundo!')

# # Exemplo int
print(3+2)

# # Uma variável é definida como no exemplo abaixo, NumberOne e NumberTwo são variáveis
NumberOne = 5
NumberTwo = 3

print(NumberOne + NumberTwo)
print('2'+'3')
print('Olá' + 5)
print('Olá', 5)

nome = 'Gabriel'
idade = 20
peso = 65

print(nome, idade, peso)

# # Função input, cria uma interação e você define o valor da variável
nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')
peso = input('Qual o seu peso?')


print('Olá', nome ,'prazer em te conhecer!')

dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')

# # Utilizar vírgula quando quiser deixar um espaço entre as strings e + quando não quiser espaço
print('Você nasceu no dia', dia, 'de', mes, 'de', ano + '.')

# Input que recece o valor na class string
number1 = input('Primeiro número ')
number2 = input('Segundo número ')

print(number1 + number2)

# Input que recece o valor na class int
number1 = int(input('Primeiro número '))
number2 = int(input('Segundo número '))

print(number1 + number2)

