"""
Palindrome class realization.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack

class Palindrome:
    """
    Palindrome ADT
    """
    @staticmethod
    def read_file(path):
        """
        Function that reads the file and writes them into the list
        """
        words = []
        with open(path) as file:
            for line in file:
                words.append(line.strip().split()[0])
        return words

    @staticmethod
    def write_to_file(path, words):
        """
        Function that writes words to the given file
        @param path:
        @param words:
        @return:
        """
        with open(path, 'w') as file:
            for word in words:
                file.write(word)
                file.write(f"\n" if word != words[-1] else "")

    @staticmethod
    def find_palindromes(source, path):
        """
        Function to find palindroms using the
        @return:
        """
        words = Palindrome.read_file(source)
        palindromes = []
        for word in words:
            append = True
            stack = ArrayStack()
            for letter in word:
                stack.push(letter)
            for letter in word:
                stack_letter = stack.pop()
                if stack_letter == letter:
                    continue
                else:
                    append = False
            if append:
                palindromes.append(word)

        Palindrome.write_to_file(path, palindromes)


if __name__ == "__main__":
    palindrome = Palindrome()
    palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
    palindrome.find_palindromes("words.txt", "palindrome_en.txt")
