from PIL import Image
import os

def redimensionar_imagen(current_path, destiny_path, rezise):
    # Abre la imagen
    image = Image.open(current_path)
    width, height = image.size
    # Aplica el algoritmo de Interpolación Bicúbica para redimensionar la imagen
    rezised_image = image.resize((width*rezise, height*rezise), Image.BICUBIC)

    # Guarda la imagen redimensionada
    rezised_image.save(destiny_path)


current_path = os.getcwd()
destiny_path = current_path + "rezised"
rezise = 4

for name in os.listdir(current_path):
    name, extension = os.path.splitext(name)

    if extension in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
        # Abro la imagen y la transformo a RBG para manipularla
        current_path = current_path + '/' + name + extension
        redimensionar_imagen(current_path, destiny_path, rezise)

        redimensionar_imagen(current_path, destiny_path, rezise)