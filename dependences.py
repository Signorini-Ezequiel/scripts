import subprocess

# Lista de todas las dependencias
dependencias = [
    "subprocess",
    "requests",
    "hashlib",
    "colorama",
    "piexif",
    "phonenumbers",
    "folium",
    "opencage",
    "rembg"
]



def instalar_dependencia(libreria):
    try:
        subprocess.check_call(['pip', 'install', libreria])
    except subprocess.CalledProcessError as e:
        print(f"No se pudo instalar la librería {libreria}. Error: \n{e}")

def instalar_dependencias_faltantes():
    print("\nIniciando chequeo de dependencias...")
    for libreria in dependencias:
        try:
            __import__(libreria)
        except ImportError:
            print(f"La libreria {libreria} no esta instalada. Instalando...")
            instalar_dependencia(libreria)
    print("Chequeo finalizado\n")