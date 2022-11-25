import sys

counter = 0

k = int(sys.argv[1])

string = sys.argv[2]

if len(sys.argv) != 3:
    print("Debes introducir una cadena válida")
if k <= 0:
    print("Introduce un número positivo distinto de 0")

word_list = string.split()

list_size = len(word_list)

for i in range(list_size):
    
    if len(word_list[i]) == k:
        counter += 1

print("Hay {} palabras de tamaño {}".format(counter, k))