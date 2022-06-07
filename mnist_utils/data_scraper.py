import wget

MNIST_TEST_URL_DATA = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
MNIST_TEST_URL_LABELS = "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"

MNIST_TRAINING_URL_DATA = "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"
MINST_TRAINING_URL_LABELS = "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"


DOWNLOAD_PATH = "../Data/"


def download_data(url: str, path: str = DOWNLOAD_PATH):
    wget.download(url, path)


if __name__ == "__main__":

    # Test set.
    download_data(MNIST_TEST_URL_DATA)
    download_data(MNIST_TEST_URL_LABELS)

    # Training set.
    download_data(MNIST_TRAINING_URL_DATA)
    download_data(MINST_TRAINING_URL_LABELS)
