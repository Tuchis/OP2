"""
MODULE DOCSTRING
"""
import sys

import numpy
import numpy as np
from PIL import Image, ImageOps


class GrayscaleImage():
    def __init__(self, nrows, ncols):
        """
        Init method
        @param nrows: number of rows
        @param ncols: number of columns
        """
        self.nrows, self.ncols = nrows, ncols
        self.photo = np.zeros((self.nrows, self.ncols))

    def __str__(self):
        """
        Str method
        @return: array
        """
        return str(self.photo)

    def width(self):
        """
        Function that returns the width of the image
        @return: number of columns
        """
        return self.ncols

    def height(self):
        """
        Function that returns the height of the image
        @return: number of rows
        """
        return self.nrows

    def clear(self, value):
        """
        Clears the image by setting the value of every pixel
        @param value: the value, that is set
        @return: None
        """
        self.photo = np.full((self.nrows, self.ncols), value)

    def getitem(self, row, col):
        """
        Returns the item, that is located at given coordinates
        @param row: the row - Y coord
        @param col: the column - X coord
        @return: value
        """
        return self.photo[row][col]

    def setitem(self, row, col, value):
        """
        Sets the value of given item
        @param row: the row - Y coord
        @param col: the column - X coord
        @return: value
        @return: None
        """
        self.photo[row][col] = value

    def from_file(self, path):
        """
        Creating the example, that is loaded from .png or .jpg file
        @param path: path to the file
        @return: None
        """
        self.photo = np.array(ImageOps.grayscale(Image.open(path)))

    def lzw_compression(self):
        """
        Compressing the file using the Lempel-Ziv-Welch algorithm
        @return: None
        """
        entries = {}
        for i in range(256):
            entries[(i,)] = i
        len_ent = 256
        compressed = []
        value = tuple()
        for number in np.ravel(self.photo):
            if value + (number, ) in entries:
                value = value + (number, )
            else:
                compressed.append(entries[value])
                entries[value + (number, )] = len(entries)
                len_ent += 1
                value = (number, )
        return np.array(compressed, dtype='uint16')


    def lzw_decompression(self):
        """
        Decompressing the file, which was compressed with the
        Lempel-Ziv-Welch algorithm
        @return: None
        """
        entries = {}
        for i in range(256):
            entries[(i,)] = i
        len_ent = 256
        decompressed = []
        # for

def main():
    """
    MAIN FUNCTION
    """
    # creating a image object
    image = Image.open(r"img.png")

    # creating greyscale image object by applying greyscale method
    image_grayscale = ImageOps.grayscale(image)
    photo = GrayscaleImage(*image_grayscale.size[::-1])

    print("The size of blank photo")
    print(sys.getsizeof(photo.photo))
    print(photo.width(), photo.height())
    print("------------")
    print("Initializing photo")
    photo.from_file(r"img.png")
    print(photo)
    print("Size of the array: ",
          photo.photo.size)
    print("Memory size of one array element in bytes: ",
          photo.photo.itemsize)
    print("The memoru usage is : ", photo.photo.itemsize * photo.photo.size)
    print("------------")
    print("Compressing the photo")
    compressed = photo.lzw_compression()
    print("Array: ",compressed)
    print("The length of the array: ", len(compressed))
    print("Size of the compressed array: ", sys.getsizeof(compressed))
    print("The difference between uncompressed and compressed: ", sys.getsizeof(photo.photo) - sys.getsizeof(compressed))
    print("Ratio of compressing: ", sys.getsizeof(compressed) / sys.getsizeof(photo.photo) * 100, "%")

if __name__ == "__main__":
    main()
