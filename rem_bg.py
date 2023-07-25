from rembg import remove
from PIL import Image

in_path = input("Enter the name of the picture: ")
out_path = "test1.png"

in_image = Image.open(in_path)
out = remove(in_image)

out.save(out_path)