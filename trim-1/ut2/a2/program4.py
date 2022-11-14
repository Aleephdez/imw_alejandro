import math
from operator import truediv
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

radius = float(sys.argv[1])

exit = False

while not exit:

    print(color.CYAN + '[+] 1. Calcular el diámetro de una circunferencia')
    print('[+] 2. Calcular el perímetro de una circunferencia')
    print('[+] 3. Calcular el área del círculo')
    print('[+] 4. Calcular las tres anteriores')
    print('[+] 5. Salir' + color.END)

    option = int((input(color.BOLD + 'Introduzca una opción:' + color.END)))

    if option == 5:

        print(color.RED + '[-] Saliendo...' + color.END)
        exit = True

    elif option == 1:

        print(color.GREEN + '[*] Diámetro =', 2*radius)

    elif option == 2:

        print(color.GREEN + '[*] Perímetro = ', 2*radius*math.pi)

    elif option == 3:

        print(color.GREEN + '[*] Área = ', (radius**2) * math.pi)

    elif option == 4:

        print(color.GREEN + '[*] Diámetro =', 2*radius)
        print('[*] Perímetro = ', 2*radius*math.pi)
        print('[*] Área = ', (radius**2) * math.pi)
        print(color.END)
        exit = True

    else:

        print(color.RED + 'Introduzca una opción válida' + color.END)