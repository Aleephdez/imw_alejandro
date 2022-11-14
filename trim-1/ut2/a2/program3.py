
import sys

#Defino una clase color para darle color a la salida de texto de forma sencilla y fácil de interpretar
class color:
   YELLOW = '\033[93m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   CYAN = '\033[96m'
   END = '\033[0m'

#Leemos la nota introducida y comprobamos que esté dentro el rango adecuado

mark = float(sys.argv[1])

if mark > 10 or mark < 0:

    print('Introduzca una nota válida. Debe estar comprendida entre 0 y 10')

#Comprobamos qué tipo de nota es
    
if mark == 10:
    print(color.YELLOW + 'Matrícula de honor' + color.END)
elif mark >= 9 and mark < 10:
    print(color.BLUE + 'Sobresaliente' + color.END)
elif mark >= 7 and mark < 9:
    print(color.CYAN + 'Notable' + color.END)
elif mark >= 5 and mark < 7:
    print(color.GREEN + 'Aprobado' + color.END)
elif mark < 5:
    print(color.RED + 'Suspenso' + color.END)