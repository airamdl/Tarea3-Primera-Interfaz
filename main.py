#Cargar 10 imágenes aleatorias de un directorio con imágenes proporcionadas en esta tarea.
#Mostrar una imagen con un cuadro de texto y un botón comprobar.
#La imagen es un caracter hiragana del idioma japonés, el nombre del fichero correspondiente a la imagen es la traducción al español (sin la extensión).
#Se deberá comprobar que ha introducido la traducción correctamente en el cuadro de texto, así con las 10 imágenes aleatorias y que no se repitan.




from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import random



def cargar_imagenes(hiragana):
    images = []
    translates = []
    for file in os.listdir(hiragana):
        if file.endswith(".png"):
            translate = file[:-4]
            ruta_imagen = os.path.join(hiragana, file)
            images.append(ruta_imagen)
            translates.append(translate)
    return images, translates














