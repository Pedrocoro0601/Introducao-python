nome = input("Digite seu nome: ")
idade = input("digite sua idade: ")
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
imc = peso/altura

print("-" * 30)
print("Este são meus dados: ")
print("nome: " ,nome)
print("idade: " ,idade, "anos")
print("altura" ,altura, "mts")
print("peso",peso, "kgs")
print("IMC; ", imc)

if imc<16:
    print("MAGREZA EXTREMA")
elif imc<18.5:
    print("MAGREZA")
elif imc<24.9:
    print("NORMAL")
elif imc<29.9:
    print("SOBREPESO")
elif imc<39.9:
    print ("OBESIDADE")
else: 
    print("OBESIDADE GRAVE")