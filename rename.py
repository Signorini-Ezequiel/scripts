import os
from colorama import Fore

def rename(current_path):
    print(Fore.BLUE + "Preparing to rename files/dirs according to settings...")

    print("-------------------------------------------")
    for root, dirs, files in os.walk(current_path, topdown=False):
        for name in files + dirs:
            if not name.startswith(".") or not name.startswith("__"):
                new_name = name.replace(" ", "_").replace("-", "_")
                current_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                
                if name != new_name:
                    os.rename(current_path, new_path)
                    print(f"Renamed: {name} -> {new_name}")
    print("-------------------------------------------\n")
    
    print("Process finished")