n1 = int(input("Primeiro segmento: "))
n2 = int(input("Segundo segmento: "))
n3 = int(input("Terceiro segmento: "))
if n1 == n2 and n1 == n3:
    print("Estes segmentos PODEM FORMAR um triângulo EQUILÁTERO.")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("Estes segmentos PODEM FORAMR um triângulo ISÓSCELES.")
else:
    print("Estes segmentos PODEM FORMAR um triângulo ESCALENO.")
