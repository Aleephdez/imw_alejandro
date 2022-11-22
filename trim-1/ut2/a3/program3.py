import sys

#Leemos el número introducido e inicializamos la variable total
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

#Por definición, los números primos deben ser positivos, así que comprobamos que el usuario haya introducido un número válido
if num1 < 0 or num2 < 0:
    print("[*] Introduce un número positivo")
    sys.exit(0)

if num1 == 0:

    print('El MCD de', num1, 'y', num2, 'es', num2)

elif num2 == 0:

    print('El MCD de', num1, 'y', num2, 'es', num1)
    
else: #En caso de no tener ningún número igual a 0, calculamos el MCD
   
   #Calculamos el máximo y mínimo entre ambos números, ya que usaremos el número
   #menor para operar sobre él
    a = max(num1, num2) 
    b = min(num1, num2)
    
    while b != 0:
        resto = b
        b = a%b
        a = resto
    
    print('[+]El MCD de', num1, 'y', num2, 'es', a)
