print('Programa IMC')

#string literal - email , nome
altura = float(input('Digite sua altura'))
peso = float(input('Digite seu Peso'))

imc = peso / (altura * altura)


if imc <= 18.5:
 print("baixo peso")
elif imc>=18.6 and imc<=24.9:
 print ("peso normal")
elif imc>=25 and imc<=29.9:
 print ("sobrepeso")
elif imc>=30 and imc<=34.9:
 print ("obesidade I")
elif imc>=35.0 and imc<=39.9:
 print ("obesidade II")
else:
 print ("obesidade III")