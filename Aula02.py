# # Tipos primitivos e saída de dados
int(), float(), bool(), str()

# # Exemplos:
int; 7, -4, 0, 9875
float; 4.5, 0.076, -15.223, 7.0
bool; True, False
str; 'Olá', '7.5', ''

# Prática
n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2

print('A soma entre', n1, 'e', n2, 'vale:', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# Prática 2:
n = (input('Digite algo '))

# Para saber se é um número
print(n.isnumeric())

# Para saber se é letra
print(n.isalpha())

# Para saber se tem letra e número
print(n.isalnum())

# Para saber se está somente com letras maiúsculas
print(n.isupper()) 

