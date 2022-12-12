import sys

#Función que se encarga de mostrar los datos del diccionario
def show_contacts(phone_book):  

    #Recorremos el diccionario e imprimimos los valores
    for name, phone in phone_book.items():
        print('{}: {}'.format(name, phone))


#Función que añade contactos al diccionario
def add_contact(phone_book, name, phone):

    #Si el nombre del contacto ya existe, no lo añadimos
    if name in phone_book:
        return print("El contacto ya existe")
    else: #Si no existe, lo añadimos junto a su número de teléfono
        phone_book[name] = phone
        return print("Se ha añadido al contacto {} con éxito".format(name))

#Función que borra un contacto
def remove_contact(phone_book, name):

    #Si el contacto no está en el diccionario, no se puede borrar
    if name not in phone_book:
        return print("El contacto no existe")
    else:   #Si está, lo borramos
        del(phone_book[name])
        return print("Se ha eliminado al contacto {} con éxito".format(name))

#Función que muestra un menú
def menu():

    #Iniciamos la variable exit a false y el diccionario
    exit = False

    phone_book = {}

    #Mostramos el menú
    print("1. Mostrar la lista de contactos")
    print("2. Añadir contacto (nombre y teléfono)")
    print("3. Borrar contacto (nombre)")
    print("4. Salir del programa")

 
    while not exit:
        
        #Leemos la opción del usuario
        option = input("Introduzca una opción: ")

        if option == '1':
            show_contacts(phone_book)   #Mostramos los contactos
        if option == '2':
             #Pedimos el contacto y el número que vamos a añadir   
            contact = input("Introduzca el nombre del contacto a añadir: ")
            number = input("Introduzca el número del contacto a añadir: ")
            add_contact(phone_book, contact, number)
        if option == '3':
            contact = input("Introduzca el nombre del contacto a eliminar: ")  #Pedimos el contacto que vamos a borrar
            remove_contact(phone_book, contact)
        if option == '4':
            exit = True #Salimos del programa

if __name__ == '__main__':
   
   menu()