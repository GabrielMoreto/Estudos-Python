# Cores no Terminal
# ANSI ecsape sequence

# 0 representa o Style, 33 Text e 44 Back
# \033[0; 33; 44m

# Style: 0: None "Sem estilo", 1: Bold "Em negrito", 4: Underline "Sublinhado", 7:Negative "Negativo"
# Text: 30: Branco, 31: Vermelho, 32: Verde, 33: Amarelo, 34: Azul, 35: Roxo, 36: Ciano, 37: Cinza
# Back: 40: Branco, 41: Vermelho, 42: Verde, 43: Amarelo, 44: Azul, 45: Roxo, 46: Ciano, 47: Cinza

# Prática
print('\033[1;30;45mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Gabriel'
cores = {'limpa':'\033[m', 
        'azul':'\033[34m', 
        'amarelo':'\033[33m,',
        'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

