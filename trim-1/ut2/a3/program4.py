import sys

#Leemos el número introducido e inicializamos la variable total
num = int(sys.argv[1])

#Por definición, los números primos deben ser positivos, así que comprobamos que el usuario haya introducido un número válido
if num < 0:
    print("[*] Introduce un número positivo")
    sys.exit(0)
elif num == 0:
    print("0! = 1")
    sys.exit(0)


for i in range(1, num+1):
    factorial = 1
    for j in range(i,0, -1):    
        factorial *= j
    
    print("{}! = {}".format(i,factorial))

