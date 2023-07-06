from PIL import Image
import os

formats = [".jpg", ".jpeg", ".png", ".bmp", ".webp", ".ico"]


print("\n")
print("Select if you want to choose the current path or a different path to change format")
print("Here: h \nOther: o\n")
current_path = input("Where: ")
while current_path != "h" and current_path != "o":
    current_path = input("Where: ")
if current_path == "h":
    current_path = os.path.dirname(os.path.abspath(__file__))
else:
    current_path = input("Enter the path:\n")

print("\n Enter the name of the directory or leave empty to save in the current path\n")
destiny_path = input("Enter the name of the destiny directory:\n")
image_path = os.path.join(current_path, destiny_path)

if destiny_path != "":
    if os.path.exists(image_path):
        while os.path.exists(image_path):
            new_destiny = input("The chosen directory name already exists, change destiny (y/n): ")
            
            while new_destiny != "n"  and new_destiny != "y":
                new_destiny = input("The chosen directory name already exists, change destiny (y/n): ")
            if new_destiny == "y":
                destiny_path = input("Enter the name of the destiny directory:\n")
                os.makedirs(image_path)
            else:
                break
    else:
        os.makedirs(image_path)
else:
    image_path = current_path
    print("Everything will be added in the current path\n")


print("Enter the final format for pictures from the list:")
for format in formats:
    print(f"- {format}")
format = input("\nEnter the final format for pictures from the list:").lower()

for name in os.listdir(current_path):
    name, extension = os.path.splitext(name)

    if extension in formats:
        # Abro la imagen y la transformo a RBG para manipularla
        picture = Image.open(f'{current_path}/{name}{extension}')
        picture = picture.convert('RGB')

        try:
            # Guardo la imagen de forma optimizada
            picture.save(os.path.join(image_path, name + format), optimize=True)
            print(f'The image {name} were saved')
        except Exception as error:
            print(f'{error}\n')