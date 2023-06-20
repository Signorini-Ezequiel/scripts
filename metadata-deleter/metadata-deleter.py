import piexif

def remove_location(image_path, output_path):
    # Cargar los metadatos de la imagen
    exif_dict = piexif.load(image_path)

    # Verificar si existen datos de ubicación (coordenadas GPS)
    if piexif.GPSIFD in exif_dict and piexif.GPSIFD in exif_dict[piexif.GPSIFD]:
        # Eliminar los datos de ubicación
        del exif_dict[piexif.GPSIFD]

    # Guardar la imagen con los metadatos modificados
    piexif.insert(piexif.dump(exif_dict), image_path, output_path)

    print("Ubicación eliminada correctamente.")

# Ejemplo de uso
image_path = "ruta/a/tu/imagen.jpg"
output_path = "ruta/a/tu/imagen_sin_ubicacion.jpg"
remove_location(image_path, output_path)
