import os
import patoolib

# File path to data.
DATA_PATH = os.getcwd() + "/../Data/"

files = os.listdir(DATA_PATH)
files = [DATA_PATH + file for file in files if file[-3:] == ".gz"]

for file in files:
    patoolib.extract_archive(file, outdir=DATA_PATH)
