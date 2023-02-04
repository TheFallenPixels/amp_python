# Made by FallenPixels.
# Runs terminal command to install all python modules.
# Recommend that this is ran in a docker container.

# When running this file please include the file you would like to execute.
# Example: python3 loader.py main.py (.py is optional in name)

# AMP USERS NOTICE: Prints must use flush=true to appear live in console.

import os
import pathlib
print("loader.py >>> Installing requirements.txt", flush=True)
os.system(f'pip install -r {pathlib.Path(__file__).parent.resolve()}/requirements.txt')
print("loader.py >>> Completed installation of requirements.txt", flush=True)

if __name__ == "__main__":
    import sys
    try:
        file = sys.argv[1]
        if not file.endswith(".py"):
            print("loader.py >>> File name did not end with \".py\". Adding...", flush=True)
            file+=".py"
        print(f"loader.py >>> Loading \"{file}\"...", flush=True)
        exec(open(f'{pathlib.Path(__file__).parent.resolve()}/{file}').read())
    except IndexError:
        print("loader.py >>> No file provided to load.", flush=True)

print("loader.py >>> Complete. Exiting...", flush=True)