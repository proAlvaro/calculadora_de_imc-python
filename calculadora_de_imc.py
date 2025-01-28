def convertor_de_valor(valor_str):
    valor_str = valor_str.replace(',','.')
    try:
        valor = float(valor_str)
        return valor
    except ValueError:
        return 'valor invalido'

peso_str = input('Digite o seu peso : ')
altura_str = input('Digite a sua altura : ')

peso = convertor_de_valor(peso_str)
altura = convertor_de_valor(altura_str)

if altura >= 100  : 
    altura = altura / 100

calculando_imc = peso / (altura*2)
calculando_imc = round(calculando_imc, 1)

if calculando_imc < 18.5 :
    print(f'seu imc foi ({calculando_imc}) = abaixo do peso ideal')
elif 24.9 >= calculando_imc >= 18.5 :
    print(f'seu imc foi ({calculando_imc}) = peso ideal')
elif 29.9 >= calculando_imc >= 25 :
    print(f'seu imc foi ({calculando_imc}) = sobre peso')
elif 34.9 >= calculando_imc >= 30 :
    print(f'seu imc foi ({calculando_imc}) = obesidad tipo 1')
elif 39.9 >= calculando_imc >= 35 :
    print(f'seu imc foi ({calculando_imc}) = obesidad tipo 2')
elif calculando_imc >= 40 :
    print(f'seu imc foi ({calculando_imc}) = obesidad tipo 3')