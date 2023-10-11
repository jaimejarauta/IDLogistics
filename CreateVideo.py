import pickle
from matplotlib import pyplot as plt
from matplotlib import colors
import ipywidgets
from ipywidgets import Layout, interact, IntSlider
from IPython.display import display, HTML
import cv2
import io
import numpy as np
from PIL import Image, ImageTk
import PIL
import os

with open("map_hour1.pickle", "rb") as handle:
    maps_loaded = pickle.load(handle)

time_list = list(maps_loaded.keys())
map_list = list(maps_loaded.values())

colormap = colors.ListedColormap(["white", "grey", "blue", "red"])

# Creamos una figura de Matplotlib con el tamaño deseado
fig = plt.figure(figsize=(12, 8))

# Generamos todas las imágenes
for i, time in enumerate(time_list):
    plt.clf()
    plt.imshow(map_list[i], cmap=colormap)
    plt.axis("off")
    plt.title(f"Time: {time}")

    # Cambiamos el tamaño de la figura
    fig.set_size_inches(12, 8)

    # Guardamos la figura en un archivo PNG
    name = f"Images/image{str(i)}.png"
    plt.savefig(name, bbox_inches="tight", pad_inches=0, dpi=100)

# Array vacío
img_array = []

# For para leer imagenes desde un directorio
for x in range(len(time_list)):
    path = f"Images/image{x}.png"
    img = cv2.imread(path)
    img_array.append(img)

# Tamaño de la última imagen alto y ancho
height, width = img.shape[:2]

num_video = 1
while True:
    video_name = f"video_sim{num_video}"
    path = f"./{video_name}.mp4"
    num_video += 1
    if not os.path.exists(path):
        break

video = cv2.VideoWriter(
    video_name,
    cv2.VideoWriter_fourcc(*"mp4v"),
    5,
    (width, height),
)

# For para guardar frames en un video
for i in range(len(img_array)):
    video.write(img_array[i])

video.release()
