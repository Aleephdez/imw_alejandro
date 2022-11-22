
import sys

#Leemos el número introducido e inicializamos la variable counter
num = int(sys.argv[1])
counter = 0

#Por definición, los números primos deben ser positivos, así que comprobamos que el usuario haya introducido un número válido
if num < 0:
    print("[*] Introduce un número positivo")
    sys.exit(0)

#El 1 y el 0 tampoco son primos
elif num == 1 or num == 0:
    print("[+] No es primo")
    sys.exit(0)

#Realizamos un bucle que divida el número introducido por todos los números que le preceden, empezando en 1 ya que no podemos dividir por 0.
for i in range(1, num+1):
    
     residual = num%i   #Si el resto de la división es 0 → num es divisible por i
     if residual == 0:  #Si num es divisible por i, sumamos uno al contador. 
         counter += 1
         if counter > 2: #Sabemos que un número primo solo tiene dos divisores, así que en el momento en el que encontremos más de dos salimos del bucle.
             print("[+] No es primo")
             sys.exit(0)

print("[+] Es primo")