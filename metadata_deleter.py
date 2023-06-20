import piexif
import os
from PIL import Image

def remove_metadata(current_path):
    print("Preparing to delete sensitive metadata from pictures...")

    for root, dirs, files in os.walk(current_path, topdown=False):
        for name in files:
            if name.lower().endswith(("jpg", "jpeg", "png", "webp")):
                # Get the full file path
                file_path = os.path.join(root, name)

                # Open the image
                picture = Image.open(file_path)

                # Load the image metadata
                exif_dict = piexif.load(picture.info["exif"])

                # Remove sensitive metadata
                exif_dict["0th"] = {}      # Camera data
                exif_dict["Exif"] = {}     # Camera configuration data (in detail)
                exif_dict["GPS"] = {}      # Location data
                exif_dict["1st"] = {}      # Manufacturer data

                # Save the image without the sensitive metadata, overwriting the original image
                picture.save(file_path, exif=piexif.dump(exif_dict))

                print("\n-------------------------------------------")
                print(f"Sensitive metadata deleted correctly from picture: {file_path}")
                print("-------------------------------------------\n")


# Test
# current_path = os.getcwd()
# remove_metadata(current_path)