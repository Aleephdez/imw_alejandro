import math
import sys

#Defino una clase color para darle color a la salida de texto de forma sencilla y fácil de interpretar
class color:
   CYAN = '\033[96m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   END = '\033[0m'

#Primero hacemos un control de errores, si el usuario no introduce 3 números salta mensaje de error personalizado:

if len(sys.argv) < 4:

    print(color.BOLD + 'Debes introducir 3 números, separados por espacios.' + color.END)

else: #Si se han introducido correctamente, leemos los valores y los almacenamos

    a = float(sys.argv[1])

    b = float(sys.argv[2])

    c = float(sys.argv[3])

    if a == 0: #Si a=0 tenemos una ecuación de primer grado, que se resuelve igualando

        print(color.GREEN + 'Se trata de una ecuación de primer grado' + color.END,'\n x =', -c/b)
        
    elif  b**2 - (4*a*c) < 0: #Si el discriminante es menor que 0, tendríamos una raíz de un número negativo en el campo de los reales. No existe

        print(color.BLUE + 'El discriminante b^2-4ac es menor que 0, por lo que no existe una solución real.' + color.END)

    else: #Resolvemos la ecuación aplicando la fórmula de Bhaskara

        print(color.CYAN + 'Se trata de una ecuación de segundo grado' + color.END,
        '\n x1 =', (-b+(math.sqrt(b**2 - (4*a*c))))/(2*a) , 
        '\n x2 =', (-b-(math.sqrt(b**2 - (4*a*c))))/(2*a))