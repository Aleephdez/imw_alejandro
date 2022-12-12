import sys

#Función que cuenta las veces que se repite una palabra en una misma frase
#y las almacena en un diccionario
def count_words(sentence):
    summary = {}
    words_list = sentence.split() #Separamos las palabras

    for word in words_list: #Introducimos las palabras en el diccionario, inicializadas a 0

            summary[word] = 0

    for word in summary:    #Recorremos el diccionario y la lista
        for word2 in words_list:
            if word == word2:   #Si la palabra del diccionario coincide con la palabra de la lista, acumulamos
            
                summary[word] += 1

    return summary 


sentence = sys.argv[1]

#Imprimimos los valores del diccionario de forma personalizada
for name, value in count_words(sentence).items():
    print(f'{name}:{value}')