#escreva um programa que leia 2 numeros inteiros e compare os
# mostrando na tela a mensagem 
# o primerio valor e maior:
# o segundo e mmaior:
#ambos sao iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O numero 1 e maior que o numero 2')
elif n2 > n1:
    print('O numero 2 e maior que o numero 1')
elif n1 == n2:
    print('Ambos sao iguais')
else:
    print('ERRO')