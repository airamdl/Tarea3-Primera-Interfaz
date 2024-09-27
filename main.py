#Cargar 10 imágenes aleatorias de un directorio con imágenes proporcionadas en esta tarea.
#Mostrar una imagen con un cuadro de texto y un botón comprobar.
#La imagen es un caracter hiragana del idioma japonés, el nombre del fichero correspondiente a la imagen es la traducción al español (sin la extensión).
#Se deberá comprobar que ha introducido la traducción correctamente en el cuadro de texto, así con las 10 imágenes aleatorias y que no se repitan.
from fnmatch import translate

import PIL
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import random



def get_hiragana_images_and_translates(hiragana):
    images = []
    translates = []
    for file in os.listdir(hiragana):
        if file.endswith(".png"):
            translate = file[:-4]
            img_route = os.path.join(hiragana, file)
            images.append(img_route)
            translates.append(translate)
    return images, translates


def show_images(imagen, translate):
    global window, label_image, entry_answer, check_button

    img = PIL.Image.open(imagen)
    img = img.resize((200, 200))
    photo = PIL.ImageTk.PhotoImage(img)

    label_image.config(image=photo)
    label_image.image = photo

    entry_answer.delete(0, tk.END)
    entry_answer.focus()



def check_answer():
    answer = entry_answer.get()
    points = 0
    if answer == translate:
        print("¡Correcto!")
        points +=1
    else:
        print("Incorrecto. La respuesta correcta es:", translate)


window = tk.Tk()
window.title("translate Hiragana")

label_imagen = ttk.Label(window)
label_imagen.pack()

entry_answer = ttk.Entry(window)
entry_answer.pack()

check_button = ttk.Button(window, text="check", command=check_answer())
check_button.pack()



image_route = "hiragana"
images, translates = get_hiragana_images_and_translates(image_route)

random_img = random.sample(images, 10)
random_translate = [translates[images.index(img)] for img in random_img]

show_images(random_img[0], random_translate[0])


index = 1

def next_img():
    global index
    if index < len(random_img):
        show_images(random_img[index], random_translate[index])
        index += 1
    else:
        print("¡Has terminado!")

next_button = ttk.Button(window, text="next", command=next_img())
next_button.pack()

window.mainloop()