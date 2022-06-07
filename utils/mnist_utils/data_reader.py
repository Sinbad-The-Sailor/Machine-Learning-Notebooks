import numpy as np
import os
import idx2numpy

DATA_PATH = os.getcwd() + "/../data/"


_training_data = DATA_PATH + "train-images-idx3-ubyte"
_training_labels = DATA_PATH + "train-labels-idx1-ubyte"
_testing_data = DATA_PATH + "t10k-images-idx3-ubyte"
_testing_labels = DATA_PATH + "t10k-labels-idx1-ubyte"


TRAINING_DATA = idx2numpy.convert_from_file(_training_data)
TRAINING_LABELS = idx2numpy.convert_from_file(_training_labels)

TESTING_DATA = idx2numpy.convert_from_file(_testing_data)
TESTING_LABELS = idx2numpy.convert_from_file(_testing_labels)
