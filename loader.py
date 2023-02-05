# Made by FallenPixels.
# Runs terminal command to install all python modules.
# Recommend that this is ran in a docker container.

# When running this file please include the file you would like to execute.
# Example: python3 loader.py main.py (.py is optional in name)

# AMP USERS NOTICE: Prints must use flush=true to appear live in console.

import os
from time import sleep
import pathlib
import traceback
import sys

try:
    import requests
except ModuleNotFoundError:
    print("loader.py >>> Getting dependencies for loader.", flush=True)
    os.system('pip install -U requests')
    sys.exit()

print("loader.py >>> Checking uninstall.txt for any modules that need removed.", flush=True)
os.system(f'pip uninstall -y -r {pathlib.Path(__file__).parent.resolve()}/uninstall.txt')
try:
    open(f"{pathlib.Path(__file__).parent.resolve()}/uninstall.txt","w",encoding="utf-8").write(requests.get("https://raw.githubusercontent.com/TheFallenPixels/amp_python/main/uninstall.txt", timeout=30).content.decode("utf-8"))
except Exception:
    print("Failed to clear uninstall.txt. Is the server online?")
print("loader.py >>> Checking uninstall.txt has been completed.", flush=True)

print("loader.py >>> Installing requirements.txt", flush=True)
os.system(f'pip install -r {pathlib.Path(__file__).parent.resolve()}/requirements.txt')
try:
    open(f"{pathlib.Path(__file__).parent.resolve()}/requirements.txt","w",encoding="utf-8").write(requests.get("https://raw.githubusercontent.com/TheFallenPixels/amp_python/main/requirements.txt", timeout=30).content.decode("utf-8"))
except Exception:
    print("Failed to clear requirements.txt. Is the server online?")
print("loader.py >>> Completed installation of requirements.txt", flush=True)

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        if not file.endswith(".py"):
            print("loader.py >>> File name did not end with \".py\". Adding...", flush=True)
            file+=".py"
        print(f"loader.py >>> Loading \"{file}\"...", flush=True)
        try:
            exec(open(f'{pathlib.Path(__file__).parent.resolve()}/{file}').read())
        except Exception:
            traceback.print_exc()
    except IndexError:
        print("loader.py >>> No file provided to load.", flush=True)

print("loader.py >>> Script has been completed. To prevent AMP from looping this will not exit. You may hit stop when you are done.", flush=True)

while True:
    sleep(1)