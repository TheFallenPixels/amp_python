# Made by FallenPixels.
# Runs terminal command to install all python modules.
# Recommend that this is ran in a docker container.

# When running this file please include the file you would like to execute.
# Example: python3 loader.py main.py (.py is optional in name)

import os
import pathlib
os.system(f'pip install -r {pathlib.Path(__file__).parent.resolve()}/requirements.txt')

if __name__ == "__main__":
    import sys
    try:
        file = sys.argv[1]
        if not file.endswith(".py"):
            file+=".py"
        os.system(f"python3 {pathlib.Path(__file__).parent.resolve()}/{file}")
    except IndexError:
        print("No main file to execute found.\nloader.py will not start a python file without this!")
print("Script has quit. Loader.py will now exit.")