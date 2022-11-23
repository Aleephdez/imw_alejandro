import sys

#Leemos el número introducido e inicializamos la variable total
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

#El MCD está definido para los números naturales, así que no admitimos negativos.
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
    
    #El objetivo del bucle es que b llegue a 0, ya que cuando llegue significará que hemos dado con el máximo divisor.
    while b != 0:
        save_value = b # guardamos el valor de b y lo actualizamos en cada iteración
        b = a%b      # calculamos el resto de la división entre a y b y lo almacenamos en b
        a = save_value   # metemos en a el valor salvado/actualizado de b para realizar la división de nuevo en la siguiente iteración
    
    print('[+]El MCD de', num1, 'y', num2, 'es', a)
