import sys

#Iniciamos la variable contador
counter = 0

#Leemos por pantalla
k = int(sys.argv[1])

string = sys.argv[2]

if len(sys.argv) != 3:
    print("Debes introducir una cadena válida")
if k <= 0:
    print("Introduce un número positivo distinto de 0")

#Separamos las palabras de la cadena para analizarlas una a una
word_list = string.split()

#Calculamos la longitud de la lista
list_size = len(word_list)

#Recorremos la lista y comprobamos si la longitud de cada palabra es igual a la cantidad introducida
for i in range(list_size):
    
    if len(word_list[i]) == k:
        counter += 1

#Imprimimos por pantalla
print("Hay {} palabras de tamaño {}".format(counter, k))