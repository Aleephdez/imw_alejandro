import random

#Generamos la secuencia ADN de forma aleatoria
NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES)for i in range(DNA_SIZE)])

#Iniciamos las variables a 0
adenine = 0
guanine = 0
cytosine = 0
thymine = 0

#Recorremos la secuencia de ADN analizando cada letra, si hay coincidencia acumulamos en la variable correspondiente
for i in sequence:
    if i == 'A':
        adenine += 1
    elif i == 'G':
        guanine += 1
    elif i == 'C':
        cytosine += 1
    elif i == 'T':
        thymine += 1

#Imprimimos resultados
print("[+] Adenine: {}".format(adenine))
print("[+] Guanine: {}".format(guanine))
print("[+] Cytosine: {}".format(cytosine))
print("[+] Thymine: {}".format(thymine))