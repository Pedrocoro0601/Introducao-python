alcool = float(input("digite o valor do alcool: "))
gasolina = float(input("digite o valor da gasolina "))
resultado = alcool/gasolina

if resultado < 0.70:
    print ("ABASTEÇA COM ALCOOL")
else:
    print ("ABASTEÇA COM GASOLINA")