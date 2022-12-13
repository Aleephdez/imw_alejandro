import sys

class color:
   CYAN = '\033[96m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

#Función que se encarga de mostrar los datos del diccionario
def show_contacts(phone_book):  

    for name, phone in phone_book.items(): #Recorremos el diccionario e imprimimos los valores
        print(color.BOLD + '{}: {}'.format(name, phone) + color.END)


#Función que añade contactos al diccionario
def add_contact(phone_book, name, phone):

    if name in phone_book: #Si el nombre del contacto ya existe, no lo añadimos
        return print(color.RED + "El contacto ya existe" + color.END)
    else: #Si no existe, lo añadimos junto a su número de teléfono
        phone_book[name] = phone
        return print(color.GREEN + "Se ha añadido al contacto {} con éxito".format(name) + color.END)

#Función que borra un contacto
def remove_contact(phone_book, name):

    if name not in phone_book: #Si el contacto no está en el diccionario, no se puede borrar
        return print(color.RED + "El contacto no existe" + color.END)
    else:   #Si está, lo borramos
        del(phone_book[name])
        return print(color.GREEN + "Se ha eliminado al contacto {} con éxito".format(name) + color.END)

#Función que muestra un menú
def menu():

    #Iniciamos la variable exit y creamos un diccionario vacío
    exit = False

    phone_book = {}

    #Mostramos el menú. Lo hacemos fuera del while para que no se repita constantemente y la salida sea más limpia.
    print(color.BOLD + "1. Mostrar la lista de contactos")
    print("2. Añadir contacto (nombre y teléfono)")
    print("3. Borrar contacto (nombre)")
    print("4. Salir del programa" + color.END)

    #Iniciamos el bucle que leerá las opciones del usuario
    while not exit:
        
        option = input("Introduzca una opción: ") #Leemos la opción del usuario

        if option == '1':   #Si introduce un 1, mostramos los contactos llamando a la función correspondiente
           
           show_contacts(phone_book)   

        elif option == '2':    #Si introduce un 2, pedimos tanto el nombre como el número del contacto a añadir y llamamos a la función correspondiente   
    
            contact = input(color.BOLD + "Introduzca el nombre del contacto a añadir: " + color.END)
            number = input(color.BOLD + "Introduzca el número del contacto a añadir: " + color.END)
            add_contact(phone_book, contact, number)

        elif option == '3':  #Si introduce un 3, pedimos el nombre del contacto a eliminar y llamamos a la función correspondiente
            
            contact = input(color.BOLD + "Introduzca el nombre del contacto a eliminar: " + color.END)  
            remove_contact(phone_book, contact)

        elif option == '4':   #Si introduce un 4, salimos del programa

            exit = True 

        else: #En cualquier otro caso, mostramos mensaje de error/ayuda

            print(color.RED + "Introduzca una opción correcta (1. (Mostrar) | 2. (Añadir) | 3. (Borrar) | 4. (Salir))" + color.END)

if __name__ == '__main__':
   
   menu()