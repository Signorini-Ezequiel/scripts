from PIL import Image
import os

print("\n")
print("Select if you want to choose the current path or a different path to compress the pictures")
print("Here: h \nOther: o\n")
current_path = input("Where: ")
while current_path != "h" and current_path != "o":
    current_path = input("Where: ")
if current_path == "h":
    current_path = os.path.dirname(os.path.abspath(__file__))
else:
    current_path = input("Enter the path:\n")


destiny_path = input("Enter the name of the destiny directory (empty for here):\n")
image_path = os.path.join(current_path, destiny_path)

if destiny_path != "":
    if os.path.exists(image_path):
        while os.path.exists(image_path):
            new_destiny = input("The chosen directory name already exists, change destiny (y/n): ")
            
            while new_destiny != "n"  and new_destiny != "y":
                new_destiny = input("The chosen directory name already exists, change destiny (y/n): ")
            if new_destiny == "y":
                destiny_path = input("Enter the name of the destiny directory (empty for here):\n")
                os.makedirs(image_path)
            else:
                break
    else:
        os.makedirs(image_path)
else:
    image_path = current_path
    print("Everything will be added in the current path\n")


image_quality = ""
while "" == image_quality:
    try:
        image_quality = int(input("Choose an image quality in percentage : "))
    except:
        print("The entered value is not a number, enter a number\n")
        image_quality = ""

label = ""
while "" == label:
    label = input("Should we add a label to the compressed picture (y/n): ")
    if "y" != label and "n" != label:
        print("Enter (y/n)\n")
        label = ""
if "y" == label:
    label = "-comp"



print("\n\n--------------------------------------")
for name in os.listdir(current_path):
    name, extension = os.path.splitext(name)

    if extension in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
        if "background" not in name:
            # Abro la imagen y la transformo a RBG para manipularla
            picture = Image.open(f'{current_path}/{name}{extension}')
            picture = picture.convert('RGB')

            try:
                # Obtengo el tamaño de la imagen
                # size = os.path.getsize(f'{current_path}/{name}{extension}')
                # print(f'Tamaño original de la imagen {name}: {size}\n')
                # size = size/image_quality
                # print(f'Tamaño final de la imagen {name}: {size}\n')

                # Guardo la imagen de forma optimizada
                picture.save(os.path.join(image_path, name + label +'.jpg'), optimize=True, quality=image_quality)
                print(f'The image {name + label} were saved')
            except Exception as error:
                print(f'{error}\n')
print("--------------------------------------\n")