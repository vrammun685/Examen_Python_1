import random

#Creamos una variable global que tendrá toda la tista de 
playlist={}
archivo="playlist.txt"
def cargar_fichero(archivo):
    fichero=open(archivo,"r")
    for linea in fichero:
        titulo, artista=linea.strip().split("-")
        playlist[titulo]=artista
    fichero.close()

def agregar_canción(titulo, artista):
    playlist[titulo]=artista

def eliminar_canción(titulo):
    playlist.pop(titulo)

def contar_canciones():
    print(len(playlist))

def ordenar_canciones():
    print(sorted(playlist.items()))

def buscar_artista(artista):
    for clave, valor in playlist.items():
        if valor==artista:
            print(clave)

def lista_atleatoria(numero):
    if(numero>len(playlist)):
        numero=len(playlist)
    #He mirado y solo aparecen unas lineas que no entiendo

def guardar_fichero(archivo):
    fichero=open(archivo,"w")
    for titulo in playlist:
        fichero.write(titulo+" - "+playlist[titulo]+"\n")
    fichero.close()

cargar_fichero(archivo)
agregar_canción("Otra noche en Miami","Bad Bunny")
agregar_canción("Columbia","Quevedo")
eliminar_canción("Otra noche en Miami")
contar_canciones()
ordenar_canciones()
buscar_artista("Quevedo")
print(playlist)
guardar_fichero(archivo) 