import requests
import hashlib
from colorama import Fore

print(Fore.BLUE + "\n-------------------------------------------")
print("Checkeador de mail")
print("-------------------------------------------\n")

def check_account(email):
    # Calcula el hash SHA-1 del correo electrónico
    sha1_hash = hashlib.sha1(email.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Hace una solicitud a la API para verificar si el hash está comprometido
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code == 200:
        # Busca el sufijo correspondiente en la respuesta
        hashes = response.text.splitlines()
        for h in hashes:
            if h.split(':')[0] == suffix:
                return h.split(':')[1]
        return 0  # No se encontró el sufijo en la respuesta
    else:
        # Se produjo un error en la solicitud a la API
        return "Error: No se pudo conectar a la API Have I Been Pwned"

# Ingresa el correo electrónico que deseas verificar
email = input("Ingresa el correo electronico: ").lower()
result = check_account(email)

if result == 0:
    print(Fore.GREEN + "La cuenta no ha sido comprometida")
elif result == "Error: No se pudo conectar a la API Have I Been Pwned":
    print(Fore.YELLOW + result)
else:
    print(Fore.RED + f"Tu cuenta ha sido comprometida {result} veces")
