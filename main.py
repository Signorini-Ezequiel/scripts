from dependences import instalar_dependencias_faltantes

# Chequea que las dependencias esten instaladas
instalar_dependencias_faltantes()

from metadata_deleter import remove_metadata
from rename import rename
import os

print("\n-------------------------------------------")
print("Starting files/dirs modification...")
print("-------------------------------------------\n")

should_rename = input("Should we rename files/dirs from here (y/n): ").lower()
should_remove_metadata = input("Should we remove sensitive metadata of images (y/n): ").lower()

print("\n\n")
if "y" == should_remove_metadata or "y" == should_rename:
    print("Getting current path...")
    current_path = os.getcwd()
    print(f"Current path set to: {current_path}")

if "y" == should_rename:
    # Rename files and folders from here according to some configurations
    rename(current_path)
    print("\n\n")
if "y" == should_remove_metadata:
    # Remove sensitive metadata from images starting here
    remove_metadata(current_path)
    print("\n\n")