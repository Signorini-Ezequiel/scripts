from PIL import Image
import os


current_path = os.path.dirname(os.path.abspath(__file__))

print("\n Compressor of images, enter the name of the directory or leave empty to save in the current path\n")
destiny_path = input("Enter the name of the directory to put the pictures:\n")
image_path = os.path.join(current_path, destiny_path)

if destiny_path != "":
    if os.path.exists(image_path):
        while os.path.exists(image_path):
            new_destiny = input("The chosen directory name already exists, change destiny (y/n): ")
            
            while new_destiny != "n"  and new_destiny != "y":
                new_destiny = input("The chosen directory name already exists, change destiny (y/n): ")
            if new_destiny == "y":
                destiny_path = input("Enter the name of the directory to put the pictures:\n")
                os.makedirs(image_path)
            else:
                break
    else:
        os.makedirs(image_path)
else:
    image_path = current_path
    print("Everything will be added in the current path\n")


target_image_size = int(input("\nElija una calidad de imagen, en tamaño (kb): "))



for name in os.listdir(current_path):
    name, extension = os.path.splitext(name)

    if extension in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
        # Abro la imagen y la transformo a RBG para manipularla
        picture = Image.open(f'{current_path}/{name}{extension}')
        picture = picture.convert('RGB')

        try:
            # Obtengo el tamaño de la imagen
            size = os.path.getsize(f'{current_path}/{name}{extension}')
            print(size)
            size = size*1024 # Convierte el tamaño a kb
            if size > target_image_size:
                size = target_image_size/size*100 # Con regla de 3 simple transforma el tamaño actual en el porcentaje requerido para que tenga el peso ingresado
                print(size)
            else:
                print("The size of the picture {imagen}, isn't bigger than the target size, omitting")

            # Guardo la imagen de forma optimizada
            picture.save(os.path.join(image_path, name + '.jpg'), optimize=True, quality=size)
            print(f'Se ha guardado la imagen {name}')
        except Exception as error:
            print(f'{error}\n')