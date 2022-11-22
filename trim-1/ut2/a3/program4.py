import sys

#Leemos el número introducido e inicializamos la variable total
num = int(sys.argv[1])

#El factorial está definido para número naturales, así que no admitimos negativos
if num < 0:
    print("[*] Introduce un número positivo")
    sys.exit(0)
#Por definición, el factorial de 0 es 1
elif num == 0:
    print("0! = 1")
    sys.exit(0)

#Hacemos dos bucles, el primero se encarga de recorrer los números de los que haremos el factorial
for i in range(1, num+1):
    factorial = 1
    for j in range(i,0, -1):    #el segundo calcula el factorial de cada número recorrido por el primer bucle
        factorial *= j
    
    print("{}! = {}".format(i,factorial))

