import math
import sys

#Primero hacemos un control de errores, si el usuario no introduce 3 números salta mensaje de error personalizado:

if len(sys.argv) < 4:

    print('Debes introducir los 3 coeficientes de la ecuación. Si alguno no existe, introduce un 0')

else: #Si se han introducido correctamente, leemos los valores y los almacenamos

    a = float(sys.argv[1])

    b = float(sys.argv[2])

    c = float(sys.argv[3])

    if a == 0: #Si a=0 tenemos una ecuación de primer grado, que se resuelve igualando

        print('Se trata de una ecuación de primer grado' '\n x =', -c/b)
        
    elif  b**2 - (4*a*c) < 0: #Si el discriminante es menor que 0, tendríamos una raíz de un número negativo en el campo de los reales. No existe

        print('El discriminante b^2-4ac es menor que 0, por lo que no existe una solución real.')

    else: #Resolvemos la ecuación aplicando la fórmula de Bhaskara

        print('Se trata de una ecuación de segundo grado',
        '\n x1 =', (-b+(math.sqrt(b**2 - (4*a*c))))/(2*a) , 
        '\n x2 =', (-b-(math.sqrt(b**2 - (4*a*c))))/(2*a))