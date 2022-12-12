import sys

# Función que cuenta el número de vocales en un texto
def num_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] #Creamos una lista con las vocales
    counter = 0 # Inicializamos el contador
    for char in text:   #Recorremos todo el texto caracter a caracter, si hay una vocal sumammos 1 al contador
        if char in vowels:
            counter += 1
    return counter  #Retornamos el contador

#Función que cuenta el número de espacios en blanco en un texto
def num_whitespaces(text):
    counter = 0
    for char in text:   #Recorremos el texto caracter a caracter, si hay un espacio en blanco sumamos 1 al contador
        if char == ' ':
            counter += 1
    return counter

#Función que cuenta el número de digitos en un texto
def num_digits(text):
    counter = 0
    for char in text:   #Recorremos el texto caracter a caracter, si es numérico sumamos 1 al contador
        if char.isnumeric() == True:
            counter += 1
    return counter

#Función que calcula el número de palabras de un texto
def num_words(text):
    word_list = text.split()    #Separamos las palabras y las metemos en una lista
    return len(word_list)   #Retornamos la longitud de la lista, que es igual al número de palabras

#FUnción que imprime el texto al revés
def reverse(text):
    string = ' ' #Creamos una cadena vacía para ir añadiendo las palabras
    for i in range(length(text)-1, -1, -1): #Bucle for que va desde la longitud del texto -1, hasta -1 en reversa
        string = string + text[i]   #Metemos las palabras de una en una en la cadena, formando el texto al revés
    return string
    
#FUnción que devuelve la longitud del texto
def length(text):
    counter = 0 
    for char in text:   #Recorremos el texto caracter a caracter y acumulamos la cantidad de caracteres
        counter += 1
    return counter

#Función que divide el texto por la mitad
def halfs(text):
    string= ''  #Definimos una cadena vacía para introducir las palabras
    half = length(text)//2  #Calculamos la mitad de la longitud del texto
    for i in range(half):   #Recorremos el texto hasta la mitad y vamos añadiendo las palabras en la cadena que hemos definido
        string = string + text[i]
    
    string = string + ' | '  #Cuando hayamos recorrido la primera mitad, añadimos el separador

    for i in range(half, length(text)): #Recorremos la segunda mitad del texto e introducimos las palabras restantes
        string = string + text[i]

    return string

#Función que imprime las palabras que contengan una letra mayúscula como mínimo
def upper_vowels(text):
    word_list = text.split()    #Dividimos el texto en palabras y lo almacenamos en una lista
    new_string = ' '    #Creamos una cadena vacía
    for i in word_list: #Recorremos las palabras de la lista
        for char in i:  #Recorremos los caracteres de cada palabra
            if char.isupper() == True: #Si hay algún caracter en mayúsucla, metemos la palabra en la cadena vacía
                new_string = new_string + ' ' + i
                break #Hacemos un break para que introduzca cada palabra una sola vez en caso de tener múltiples mayúsuculas
    return new_string
        
#FUnción que ordena las palabras alfabéticamente
def sorted_by_words(text):
    word_list = text.split()    #Separamos las palabras
    word_list.sort()    # Las ordenamos alfabéticamente con la función sort
    new_string = ' '.join(word_list)    #Convertimos la lista ya ordenada en un string y la retornamos
    return new_string

#Función que devuelve la longitud de cada palabra
def length_of_words(text):
    length_list = []    #Creamos una lista vacía para introducir la longitud de cada palabra
    word_list = text.split()    #Separamos las palabras
    for i in word_list: #Recorremos las palabras de la lista
        counter = 0 #Reiniciamos a 0 la variable counter en cada iteración
        for char in i:  #Recorremos los caracteres de cada palabra
            counter += 1    #Acumulamos el número de caracteres por palabra
            number = str(counter)   #Transformamos el número en un string, para poder convertir la lista en un string posteriormente
        length_list.append(number)  #Añadimos el número a la lista vacía
    
    new_string = ' '.join(length_list)  #Transformamos la lista en un string

    return new_string


if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))
