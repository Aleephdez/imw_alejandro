import sys

#Leemos el número introducido e inicializamos la variable total
num = int(sys.argv[1])
total = 0

#Vamos a requerir un número positivo
if num < 0:
    print("[*] Introduce un número positivo")
    sys.exit(0)

#Calculamos el cuadrador de cada número y acumulamos el resultado en total.   
for i in range(1,num+1):
   total += i**2


print("{}".format(total))
