import os
import re

def rename_folders_recursive(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for folder in dirnames:
            # Ignorar carpetas ocultas
            if folder.startswith('.'):
                continue
            
            # Obtener el nuevo nombre aplicando las modificaciones
            new_name = folder.lower().replace(' ', '-').replace('y', '').replace('de', '')
            new_name = re.sub('-+', '-', new_name)  # Eliminar posibles múltiples guiones
            
            # Obtener la ruta completa de la carpeta actual
            old_path = os.path.join(dirpath, folder)
            new_path = os.path.join(dirpath, new_name)
            
            # Renombrar la carpeta
            os.rename(old_path, new_path)
            print(f'Renombrada: {old_path} -> {new_path}')
        
        # Actualizar la lista de nombres de carpetas para incluir los cambios realizados
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

# Directorio raíz desde donde se iniciarán los cambios de nombre en cascada
root_directory = os.getcwd()

# Llamar a la función para renombrar las carpetas en cascada
rename_folders_recursive(root_directory)