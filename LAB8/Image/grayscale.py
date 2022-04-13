"""
MODULE DOCSTRING
"""
import os.path
import sys
import numpy
import numpy as np
import inspect
from PIL import Image, ImageOps


class GrayscaleImage():
    def __init__(self, nrows=1, ncols=1):
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
        assert isinstance(value, int) and 0 <= value <= 255, "Wrong value"
        self.photo = np.full((self.nrows, self.ncols), value)

    def getitem(self, row, col):
        """
        Returns the item, that is located at given coordinates
        @param row: the row - Y coord
        @param col: the column - X coord
        @return: value
        """
        assert isinstance(row, int) and 0 <= col <= 255, "Wrong row value"
        assert isinstance(col, int) and 0 <= col <= 255, "Wrong column value"
        return self.photo[row][col]

    def setitem(self, row, col, value):
        """
        Sets the value of given item
        @param row: the row - Y coord
        @param col: the column - X coord
        @return: value
        @return: None
        """
        assert isinstance(value, int) and 0 <= value <= 255, "Wrong value"
        assert isinstance(row, int) and 0 <= col <= 255, "Wrong row value"
        assert isinstance(col, int) and 0 <= col <= 255, "Wrong column value"
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
        First, the file is turned into the ascii table chars, which is possible
        due to the maximum value of table - 255.
        After that we have LZW compression for strings.
        @return: None
        """
        # Initializing dictionary for LZW
        dict_size = 256
        table = {chr(i): i for i in range(dict_size)}

        # Converting integers into the string
        line = ""
        for number in np.ravel(self.photo):
            line += chr(number)

        # LZW compression
        value = ""
        result = []
        for element in line:
            key = value + element
            if key in table:
                value = key
            else:
                result.append(table[value])
                table[key] = dict_size
                dict_size += 1
                value = element
        if value:
            result.append(table[value])

        # Optimising space for small files
        if max(result) <= 2**16:
            result = np.array(result, dtype='uint16')
        else:
            result = np.array(result, dtype='uint32')

        # Defining compressed in the class
        self.compressed = result

        return result


    def lzw_decompression(self):
        """
        Decompressing the file using the Lempel-Ziv-Welch algorithm
        We decompress the file that we compressed before
        @return: None
        """
        # We are using the StringIO to prevent time losses
        # The time complexity of string concatenation
        # using operator + is O(n²)
        # We prevent it by using that library
        from io import StringIO

        # Initializing dictionary
        dict_size = 256
        table = {i: chr(i) for i in range(dict_size)}

        result = StringIO()
        compressed = list(self.compressed)
        element = chr(compressed.pop(0))
        result.write(element)

        # LZW decompression
        for key in compressed:
            if key in table:
                value = table[key]
            elif key == dict_size:
                value = element + element[0]
            else:
                raise ValueError('Bad compressed k: %s' % key)
            result.write(value)
            table[dict_size] = element + value[0]
            dict_size += 1
            element = value

        # Unpacking the StringIO object
        result = result.getvalue()
        table = {chr(i): i for i in range(dict_size)}
        line = ""
        for elem in result:
            line += str(table[elem]) + " "
        return np.array([int(i) for i in line.strip().split()], dtype="uint8").reshape((self.height(), self.width()))

    """
    Following LZW are very slow and are using integers and tuples instead of
    strings in realisation. They're not worth to look at

    def lzw_compression(self):
        entries = {}
        for i in range(256):
            entries[(i,)] = i
        len_ent = 257
        compressed = []
        value = tuple()
        entries[np.ravel(self.photo)[0], np.ravel(self.photo)[1]] = 256
        for number in np.ravel(self.photo):
            if value + (number, ) in entries:
                value = value + (number, )
            else:
                compressed.append(entries[value])
                entries[value + (number, )] = len_ent
                len_ent += 1
                value = (number, )
        compressed += value
        if max(compressed) <= 2**16:
            self.compressed = np.array(compressed, dtype='uint16')
        else:
            self.compressed = np.array(compressed, dtype='uint32')
        return self.compressed

    def lzw_decompression(self):
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
    """

def main():
    """
    MAIN FUNCTION
    """
    # Creating an image object
    file = r"img.png"
    try:
        image = Image.open(file)
    except FileNotFoundError:
        assert False, "Wrong path"

    # Creating greyscale image object by applying greyscale method
    image_grayscale = ImageOps.grayscale(image)
    photo = GrayscaleImage(*image_grayscale.size[::-1])
    photo.clear(12)

    # Info
    print("The size of blank photo")
    print(sys.getsizeof(photo.photo))
    print(photo.width(), photo.height())

    # Initializing
    print("------------")
    print("Initializing photo")
    photo.from_file(file)
    print(photo)
    print(f"Number of elements: {numpy.size(photo.photo)}")
    print(f"Size: {sys.getsizeof(photo.photo)}")
    print("------------")

    # Compressing
    print("Compressing the photo")
    compressed = photo.lzw_compression()
    print("Array: ",compressed)
    print("The length of the array: ", len(compressed))
    print("The difference between uncompressed and compressed: ", photo.photo.size - len(compressed), "elements")
    print("Ratio of compressing in elements: ", len(compressed) / photo.photo.size * 100, "%")
    print(f"Size: {sys.getsizeof(compressed)}")
    print(f"Ratio of compressing in size: {sys.getsizeof(compressed)/sys.getsizeof(photo.photo) * 100} %")
    print("-------------")

    # Decompressing
    print("Decompressing of the photo")
    decompressed = photo.lzw_decompression()
    print(photo)
    print("Comparison with the staring file:")
    print(decompressed == photo.photo)
    print("------------")

    # Visualising the unpacked photo
    image = Image.fromarray(decompressed)
    image.save(f"{os.path.basename(file).split('.')[0]}_grayscaled.{os.path.basename(file).split('.')[-1]}")
    image.show()

if __name__ == "__main__":
    main()
