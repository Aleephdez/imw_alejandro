import sys

#Creamos la lista con la letra que corresponde a cada número del 0 al 22
letter_list = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X'
, 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

#Leemos el DNI por pantalla
id = int(sys.argv[1])

#Si tomamos el DNI como un entero (8 cifras), es un número que va estar comprendido entre 10.000.000 (10 millones) y 100.000.000 (100 millones)
#Por tanto, hacemos la siguiente comprobación para ver si el número es correcto o no (tiene 8 cifras)
if id < 10000000 or id >= 100000000:
    print("[*] Introduce un DNI válido. Deben ser 8 dígitos, sin la letra")
    sys.exit(0)

#Calculamos la posición de la letra con el resto de DNI/23
letter_num = id % 23

print("{}""{}".format(id,letter_list[letter_num]))
