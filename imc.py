massa = float(input("Digite o valor da massa em (kg) : "))
altura =float(input("Digite a sua altura (m)"))

IMC = massa/altura **2
print("o seu e imc é {:.2f}" .format (IMC))

if IMC <17 :
    print("Está muito baixo o peso")
elif IMC >17 and IMC >18.5:
    print("Abaixo do peso")
elif IMC >18.5 and IMC <= 25:
    print("Peso ideal .")
elif IMC >25 and IMC <= 30:
    print("sobrepeso")
elif IMC >30 and IMC <= 35 :
    print("obesidade vai treinar")
elif IMC >35 and IMC <= 40 :
    print("obesidade severa, procura um médico")
else: 
    print("obesidade Mórbida")
