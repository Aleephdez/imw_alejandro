import sys

#Leemos el número introducido e inicializamos la variable total
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

#Por definición, los números primos deben ser positivos, así que comprobamos que el usuario haya introducido un número válido
if num1 < 0 or num2 < 0:
    print("[*] Introduce un número positivo")
    sys.exit(0)

