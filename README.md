# MnistToImgFiles
Small python 3 tool to load the MNIST dataset from keras and save each entry to a .png file.
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
python3 main.py ./mnist/images/ test 0 100
```
This will create 100 png files in ./mnist/images/ containing the first 100 handwritten numbers of the MNIST dataset
