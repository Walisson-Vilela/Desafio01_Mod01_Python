import processalista


# print('Questao 01\n ')

# nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano',
#          'Julieta', 'Maria', 'Fernando', 'Cláudio']
# # estrutura que irá armazenar o número de letras de cada nome
# qtd_letras = {}
# # calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
# for nome in nomes:
#     qtd_letras[nome] = len(nome)
# print(qtd_letras)

# print('\nQuestao 02\n ')

# nomes = {1: 'Maria', 2: 'Julieta', 3: 'Fernando', 4: 'Cristiano',
#          5: 'Julieta', 6: 'Maria', 7: 'Fernando', 8: 'Claudio'}

# print(nomes)

# print('\nQuestao 03\n ')

# # Função Implicita


# def areaCirculo(r, pi):
#     area = pi * (r ** 2)
#     return area


# print(areaCirculo(8, 3.14))

# # Funcao Expicita

# r = 8
# pi = 3.14
# area = 0


# def areaCirculo_expicita():
#     area = pi * (r ** 2)
#     return area


# print(areaCirculo_expicita())

# print('\nQuestao 04\n ')

# # area = lambda r,pi: pi * (r ** 2)


# def area(r, pi): return pi * (r ** 2)


# print(area(8, 3.14))

# print('\nQuestao 05\n ')
# lista = [3, 5, 9, 11, 12]

# print(processalista.maior_impar(lista))
# print(processalista.menor_impar(lista))

print('\nQuestao 06\n ')

cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}

dias = (int(input("Informe se deseja duas(2) consultas, ou tres(3) na semana: ")))

if(dias == 2):
    def disp_dois_especialistas(medico01, medico02):
        intersectionAB = (medico01 & medico02)
        return intersectionAB
    print(disp_dois_especialistas(ortopedista, neurologista))
elif(dias == 3):
    def disp_tres_especialistas(medico01, medico02, medico03):
        intersectionCDE = (medico01 & medico02) & (medico01 & medico03) & (medico03 & medico02)
        return intersectionCDE
    print(disp_tres_especialistas(dermatologista,neurologista,psiquiatra))






