# MnistToImgFiles
Small python 3 tool to load the MNIST dataset from keras and save each entry to a .png file using matplotlib.
This might be helpful if you are building a neural network for handwriting detection using the MNIST dataset and want to look at the numbers represented by the data quickly.

## Usage
```
python3 main.py [destination dir] [mode] [start index] [end index]
        where   destination dir must be a valid directory name (default: ./mnist_images/)
                    (if it does not exist, it will be created)
                mode must be either test or train (default: test)
                start index must be an integer (default: 0)
                end index must be an integer (default: 50)
```

## Example usage
```python
python3 main.py ./mnist_images/ test 0 5
```
This will create 5 png files in ./mnist_images/ containing the first 5 handwritten numbers of the MNIST dataset

## Result
```
.
├── main.py
└── mnist_images
    └── test
        ├── mnist_test_0-7.png
        ├── mnist_test_1-2.png
        ├── mnist_test_2-1.png
        ├── mnist_test_3-0.png
        └── mnist_test_4-4.png
```
## Images
The resulting images are created using matplotlib and look like the following: (mnist_test_0-7.png)
![alt text](https://raw.githubusercontent.com/yoshc/MnistToImgFiles/master/mnist_images/test/mnist_test_0-7.png)
