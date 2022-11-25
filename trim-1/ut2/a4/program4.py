import sys

#Inicializamos la variable que sumará todos los valores de la lista como un float
total_add = 0.0

#Leemos la lista de números
number_list= sys.argv

#Sacamos el primer elemento de la lista, que es el nombre del fichero
number_list.pop(0)

#Calculamos el tamaño de la lista para hacer la media más adelante
list_size = len(number_list)

#Recorremos la lista, convirtiendo cada número en un float y acumulándolo en una variable
for i in number_list:
    number = float(i)
    total_add += number

#Calculamos la media e imprimimos
average = total_add / list_size

print("La media de los valores es {}".format(average))