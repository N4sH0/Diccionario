import time

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'CREEPY': 'Aterrador, siniestro',
            'TILT': 'Ponerse muy agresivo/enojado',
            'GG': 'Avreviatura de good game (buen juego)',
            }

print('hola')
time sleep(1)
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('La palabra no ha sido encontrada en el diccionario')
