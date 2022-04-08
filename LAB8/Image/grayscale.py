"""
MODULE DOCSTRING
"""
import numpy


class GrayscaleImage():
    def __init__(self, nrows, ncols):
        """
        Init method
        @param nrows: number of rows
        @param ncols: number of columns
        """
        self.nrows, self.ncols = nrows, ncols
        self.photo = numpy.zeros((self.nrows, self.ncols))

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
        pass

    def getitem(self, row, col):
        """
        Returns the item, that is located at given coordinates
        @param row: the row - Y coord
        @param col: the column - X coord
        @return: value
        """
        pass

    def setitem(self, row, col, value):
        """
        Sets the value of given item
        @param row: the row - Y coord
        @param col: the column - X coord
        @return: value
        @return: None
        """
        pass

    def from_file(self, path):
        """
        Creating the example, that is loaded from .png or .jpg file
        @param path: path to the file
        @return: None
        """
        pass

    def lzw_compression(self):
        """
        Compressing the file using the Lempel-Ziv-Welch algorithm
        @return: None
        """
        pass

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
    photo = GrayscaleImage(10,15)
    print(photo)

if __name__ == "__main__":
    main()
