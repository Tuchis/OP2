"""
MODULE DOCSTRING
"""
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
            entries[i] = [i]
        compressed = []
        value = []
        for number in np.ravel(self.photo):
            if value + [number] in list(entries.values()):
                value = value + [number]
            else:
                compressed.append(list(entries.values()).index(value))
                entries[len(entries)] = value + [number]
                value = [number]
        return len(compressed)


    def lzw_decompression(self):
        """
        Decompressing the file, which was compressed with the
        Lempel-Ziv-Welch algorithm
        @return: None
        """
        pass

def main():
    """
    MAIN FUNCTION
    """
    # creating a image object
    image = Image.open(r"img.png")

    # creating greyscale image object by applying greyscale method
    image_grayscale = ImageOps.grayscale(image)

    photo = GrayscaleImage(*image_grayscale.size[::-1])
    print(photo.width(), photo.height())
    photo.from_file(r"img.png")
    photo.setitem(299,285, 255)
    print(photo.getitem(299,285))
    print(photo)
    print(photo.lzw_compression())

if __name__ == "__main__":
    main()
