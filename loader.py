# Made by FallenPixels for Scaleworx.
# Runs terminal command to install all python modules.
# Recommend that this is ran in a docker container.

# When running this file, please include the file you would like to launch.
# Example: python3 loader.py main(.py) <- .py is optional

import os;
stream = os.popen('pip install -r requirements.txt');
print(stream.read());

if __name__ == "__main__":
    import sys;
    try:
        file = sys.argv[1];
        if not file.endswith(".py"):
            file+=".py";
        exec(open(file,encoding="utf-8").read());
    except IndexError:
        print("No main file to execute found.\nloader.py will not start a python file without this!");
