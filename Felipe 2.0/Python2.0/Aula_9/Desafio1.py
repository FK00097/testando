#crie um programa que leia duas notas de um aluno e calcule a media, mostrando uma das mensagens ao
#final
#abaixo de 5 - reprovado
#5.1 e 6.9 - recuperaçao
#7 ou mais - aprovado
aluno = input('Digite seu número de aluno: ')
nota1 = int(input('Digite sua nota do primeiro semestre: '))
nota2 = int(input('Digite sua nota do segundo semestre:'))

notafinal = (nota1 + nota2)/ 2
if notafinal <= 5:
    print('Reprovado!')
elif notafinal >5 and notafinal <=6.9:
    print('Recuperação!')
else:
    print('Aprovado!')
print(f'O aluno {aluno} está com uma nota de {notafinal}!')