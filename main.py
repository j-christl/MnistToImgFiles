# Small python 3 tool to load the MNIST dataset from keras
# and save each entry to a *.png file
# used libs:    - keras
#               - matplotlib
#
# github.com/yoshc/

from keras.datasets import mnist
import matplotlib.pyplot as plt
from os import path, makedirs
from sys import argv
from sys import stdout

# standard variables
DIRECTORY = "./mnist_images/"
MODE = "TEST" # can be TEST or TRAIN
INDEX_FROM = 0
INDEX_TO = 50


# usage: python3 main.py [destination dir] [mode] [start index] [end index]
#   where   mode must be either test or train (default: test)
#           start index must be an integer (default: 0)
#           end index must be an integer (default: 50)
def main():
    global DIRECTORY, MODE, INDEX_FROM, INDEX_TO
    if len(argv) >= 5:
        INDEX_TO = int(argv[4])
    if len(argv) >= 4:
        INDEX_FROM = int(argv[3])
    if len(argv) >= 3:
        MODE = argv[2].upper()
    if len(argv) >= 2:
        if argv[1] == "--help":
            print_help()
            return
        else:
            DIRECTORY = argv[1]
    write_images()
    pass


def write_images():
    global DIRECTORY, MODE, INDEX_FROM, INDEX_TO

    dir_train = DIRECTORY + "train/"
    dir_test = DIRECTORY + "test/"
    dir_mode = dir_train if MODE == "TRAIN" else dir_test

    # Validate input
    MODE = MODE.upper()
    if not (MODE == "TRAIN" or MODE == "TEST"):
        raise ValueError('Invalid mode. Must be either TRAIN or TEST')
    if INDEX_FROM > INDEX_TO:
        raise ValueError('Invalid indices. INDEX_FROM can not be greater than INDEX_TO')

    # Load MNIST data
    print("Loading MNIST data ..")
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # Create needed directories
    if not path.exists(dir_mode):
        print("Directory does not exist. Creating it ..")
        makedirs(dir_mode)

    print("Using data entries from line", INDEX_FROM, "to", INDEX_TO, ", resulting in", str(INDEX_TO - INDEX_FROM),
          "images")
    print("Saving images to", dir_mode)
    for index in range(INDEX_FROM, INDEX_TO):
        entry = x_train[index] if MODE == "TRAIN" else x_test[index]
        number = y_train[index] if MODE == "TRAIN" else y_test[index]
        plt.imshow(entry, cmap="gray")
        plt.savefig(dir_mode + "mnist_" + MODE.lower() + "_" + str(index) + "-" + str(number) + ".png")
        print(str(index), " ", sep="", end="")
        stdout.flush()


def print_help():
    print("""usage: python3 main.py [destination dir] [mode] [start index] [end index]
        where   destination dir must be a valid directory name (default: ./mnist_images/)
                    (if it does not exist, it will be created)
                mode must be either test or train (default: test)
                start index must be an integer (default: 0)
                end index must be an integer (default: 50)""")


if __name__ == "__main__":
    main()
