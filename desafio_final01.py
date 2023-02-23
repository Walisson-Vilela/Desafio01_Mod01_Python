print('Questao 01\n ')

nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano',
         'Julieta', 'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
for nome in nomes:
    qtd_letras[nome] = len(nome)
print(qtd_letras)

print('\nQuestao 02\n ')

nomes = {1: 'Maria', 2: 'Julieta', 3: 'Fernando', 4: 'Cristiano',
         5: 'Julieta', 6: 'Maria', 7: 'Fernando', 8: 'Claudio'}

print(nomes)

print('\nQuestao 03\n ')

# Função Implicita


def areaCirculo(r, pi):
    area = pi * (r ** 2)
    return area


print(areaCirculo(8, 3.14))

# Funcao Expicita

r = 8
pi = 3.14
area = 0


def areaCirculo_expicita():
    area = pi * (r ** 2)
    return area


print(areaCirculo_expicita())
