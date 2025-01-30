#desenvolva uma logica que leia altura e peso de alguem
#calcule imc e diga o estato com:
#- de 18.5 abaixo do peso
#entre 18.5 e 25 ideal
#25 ate 30: sobrepeso
#30 ate 40: obesidade 
#acima de 40: obesidade morbida

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))

imc = peso / (altura ** 2)

if imc <=18.5:
    print('Você esta abaixo do peso! ')
elif imc > 18.5 and imc <= 25:
    print ('Você esta no peso ideal!')
elif imc > 25 and imc <= 30:
    print('Voce esta acima do peso!')
elif imc > 30 and imc <= 40:
    print('Você esta com obesidade!')
else:
    print('Você esta com obesidade morbida!')
print (imc)