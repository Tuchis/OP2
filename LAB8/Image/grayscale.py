"""
MODULE DOCSTRING
"""
import sys
import math

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
        entries[np.ravel(self.photo)[0], np.ravel(self.photo)[1]] = len_ent
        len_ent += 1
        for number in np.ravel(self.photo):
            if value + (number, ) in entries:
                value = value + (number, )
            else:
                compressed.append(entries[value])
                if len_ent == 2 ** 16:
                    len_ent = 256
                if len(entries) - len_ent >= 256:
                    del entries[list(entries.keys())[len_ent]]# 179 175 174 171 168 167 166 164 163 162
                entries[value + (number, )] = len_ent
                len_ent += 1
                value = (number, )
        compressed += value
        self.compressed = np.array(compressed, dtype='uint16')
        return self.compressed


    def lzw_decompression(self):
        """
        Decompressing the file, which was compressed with the
        Lempel-Ziv-Welch algorithm
        @return: None
        """
        entries = {}
        for i in range(256):
            entries[i] = (i, )
        entries_cursor = 257
        entries[256] = (171, 168)
        decompressed = tuple()
        value = self.compressed[0]
        decompressed += entries[int(value)]
        value = entries[int(value)]

        def unpack(entries_local):
            result = ()
            for elem_local in entries_local:
                if elem_local > 255:
                    result += (unpack(entries[elem_local]),)
                else:
                    result += (int(elem_local),)
            return result

        for i in range(1, len(self.compressed)):
            new = int(self.compressed[i])
            if new in entries:
                entry = entries[new]
                if isinstance(entry, tuple) or isinstance(entry, np.ndarray):
                    for elem in entry:
                        if elem > 255:
                            decompressed += unpack(entries[int(elem)])
                        else:
                            decompressed += (int(elem), )
                else:
                    if entry > 255:
                        decompressed += (int(entries[int(entry)]),)
                    else:
                        decompressed += (int(entry),)
                add = value + (entry[0], ) if isinstance(entry, tuple) else (entry, )
                value = entry
            else:
                entry = value + (value[0], )
                decompressed += entry
                for elem in entry:
                    if elem >= 255:
                        print(entry)
                add = entry
                value = entry
            entries[entries_cursor] = add
            entries_cursor += 1
        return np.array(decompressed, dtype='uint8').reshape((self.height(), self.width()))


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
    print("The memory usage is : ", photo.photo.itemsize * photo.photo.size)
    print("------------")
    print("Changing some values ot have better tests")
    photo.photo[0][3] = 175
    photo.photo[0][4] = 175
    photo.photo[0][5] = 175
    photo.photo[0][6] = 175
    print("Compressing the photo")
    compressed = photo.lzw_compression()
    print("Array: ",compressed)
    print("The length of the array: ", len(compressed))
    print("Size of the compressed array: ", sys.getsizeof(compressed))
    print("The difference between uncompressed and compressed: ", sys.getsizeof(photo.photo) - sys.getsizeof(compressed))
    print("Ratio of compressing: ", sys.getsizeof(compressed) / sys.getsizeof(photo.photo) * 100, "%")
    #Decompressing
    print("-------------")
    print("Decompressing of the photo")
    decompressed = photo.lzw_decompression()
    print(photo)
    print(decompressed)
    print(len(decompressed))
    print("Size of the array: ",
          decompressed.size)
    print("Memory size of one array element in bytes: ",
          decompressed.itemsize)
    print("The memoru usage is : ", decompressed.itemsize * decompressed.size)
    print(decompressed == photo.photo)
    print("------------")

if __name__ == "__main__":
    main()
