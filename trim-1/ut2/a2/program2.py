import math
import sys

#Defino una clase color para darle color a la salida de texto de forma sencilla y fácil de interpretar
class color:
   CYAN = '\033[96m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   END = '\033[0m'

#Primero hacemos un control de errores, si el usuario no introduce 6 números salta mensaje de error personalizado:

if len(sys.argv) < 7:

    print(color.BOLD + 'Debes introducir 6 números, separados por espacios. Cada par de números (x, y) representa un punto.' + color.END)

else: #Si se han introducido correctamente, leemos los valores y los almacenamos

   x1 = float(sys.argv[1])

   y1 = float(sys.argv[2])

   x2 = float(sys.argv[3])

   y2 = float(sys.argv[4])

   x3 = float(sys.argv[5])

   y3 = float(sys.argv[6])

#Calculamos la distancia a ambos puntos y comparamos

   point1_distance = math.sqrt( ((x1 - x2)**2) + ((y1-y2)**2) )

   point2_distance = math.sqrt( ((x1 - x3)**2) + ((y1-y3)**2) )

   if point1_distance < point2_distance:
      print(color.CYAN + 'El punto más cercano a ('f'{x1}'', 'f'{y1}'') es ('f'{x2}'', 'f'{y2}'') a distancia 'f'{point1_distance}' + color.END) 
   else:
      print(color.CYAN + 'El punto más cercano a ('f'{x1}'', 'f'{y1}'') es ('f'{x3}'', 'f'{y3}'') a distancia 'f'{point1_distance}' + color.END) 