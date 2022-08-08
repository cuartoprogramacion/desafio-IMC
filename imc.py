#Patricio Carrasco

print("sistema para calcular su IMC")
peso = int(input("ingrese su peso en kilogramos: "))
altura1 = int(input("ingrese su altura en centimetros: "))
altura = altura1/100
IMC = peso/(altura**2)
print(IMC)

if IMC >= 0 and IMC <= 18.4 :
    print (f"su IMC es:{IMC} La clasificación OMS es: Bajo Peso")
elif IMC >= 18.5 and IMC <= 24.99 :
    print (f"su IMC es:{IMC} La clasificación OMS es: Adecuado")
elif IMC >= 25 and IMC <= 29.99:
        print (f"su IMC es:{IMC} La clasificación OMS es: Sobre peso")
elif IMC >= 30 and IMC <= 34.99 :
        print (f"su IMC es:{IMC} La clasificación OMS es: Obesidad Grado I")
elif IMC >= 35 and IMC <= 39.99:
        print (f"su IMC es:{IMC} La clasificación OMS es: Obresidad Grado II")
elif IMC >= 40.00:
        print (f"su IMC es:{IMC} La clasificación OMS es: obesidad morbida")
else:
    print("ingrese un valor valido...")
