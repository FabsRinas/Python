peso = float(input("Digite o seu peso (Kg): "))
alt = float(input("Digite sua altura (M): "))
imc = peso / (alt ** 2)
print("O seu IMC é de {:.1f}".format(imc))
if imc <= 18.5:
    print("Você está abaixo do peso.")
elif imc <= 25:
    print("Você está com o peso ideal.")
elif imc <=30:
    print("Você está sobrepeso.")
elif imc <=40:
    print("Você está obeso.")
else:
    print("Você está com obesidade mórbida.")
