import os
import patoolib

# File path to data.
DATA_PATH = os.getcwd() + "/../Data/"

files = os.listdir(DATA_PATH)
files = [DATA_PATH + file for file in files if file[-3:] == ".gz"]

if __name__ == "__main__":

    for file in files:
        patoolib.extract_archive(file, outdir=DATA_PATH)
