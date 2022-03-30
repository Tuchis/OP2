class NullException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class WrongInput(NullException):
    pass


class CursorError(NullException):
    pass


class HomeError(NullException):
    pass


class FileIsNotRight(NullException):
    pass


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = "document.txt"

    def insert(self, character):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        try:
            del self.characters[self.cursor.position]
        except IndexError:
            raise CursorError("Cursor can't delete the non-existing character")

    def save(self):
        try:
            with open(self.filename, "w") as f:
                f.write("".join((str(c) for c in self.characters)))
        except FileNotFoundError:
            raise FileIsNotRight("The file isn't valid")

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1
        if self.position > len(self.document.characters):
            raise CursorError(
                "Cursor is in the last position, you can't move it forward anymore")

    def back(self):
        self.position -= 1
        if self.position < 0:
            raise CursorError(
                "Cursor is in the first position, you can't move it back anymore")

    def home(self):
        try:
            while self.document.characters[self.position - 1].character != "\n":
                self.position -= 1
                if self.position == 0:
                    # Got to beginning of file before newline
                    break
        except IndexError:
            raise HomeError(
                "Cursor is in the first position, you can't use home method")

    def end(self):
        while (
                self.position < len(self.document.characters)
                and self.document.characters[self.position].character != "\n"
        ):
            self.position += 1


class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        try:
            assert len(character) == 1
        except AssertionError:
            raise WrongInput("Your input is wrong")
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character


d = Document()
d.insert('h')
d.cursor.back()
d.delete()
d.insert('e')
d.cursor.home()
d.delete()
d.insert('e')
d.insert(Character('1', bold=True))
d.insert(Character('1', bold=True))
d.insert(Character('1', bold=True))
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
d.cursor.end()
d.insert('l')
d.insert('d')
print(d.string)
d.save()
