"""
MODULE DOCSTRING
"""
import sys

import note


class Notebook:
    """
    The class that contains notes
    """

    def __init__(self):
        self.notes = []
        self.note_id = 1

    def __str__(self):
        return f"The notebook\n" \
               f"There are {len(self.notes)} in the notebook"

    def print_notes(self):
        for note in self.notes:
            print(note)


    def search_by_text(self, filter) -> list:
        """
        Search by the text among the notes
        """
        match = []
        [match.append(elem.note_id) for elem in self.notes if elem.match(filter)]
        if match:
            print(f'The text is found in that notes - {str(match)[1:-1]}.')
        else:
            print(f"The text wasn't found in notes.")

    def search_by_tags(self, filter) -> list:
        """
        Search by the tags among the notes
        """
        match = []
        [match.append(elem.note_id) for elem in self.notes if elem.tags_filter(filter)]
        if match:
            print(f'Notes with such tags - {str(match)[1:-1]}.')
        else:
            print(f"There are no notes with such tags.")

    def new_note(self, memo, tags=""):
        """
        Creates the new note
        """
        self.notes.append(note.Note(memo, tags, self.note_id))
        self.note_id += 1

    def modify_memo(self, given_id, memo):
        """
        Modifies the memo in notes by its id
        """
        [note.memo_change(memo) for note in self.notes if str(note.note_id) == given_id]

    def modify_tags(self, given_id, tags):
        """
        Modifies the memo in notes by its tag
        """
        [note.tags_change(tags) for note in self.notes if str(note.note_id) == given_id]

    def print_note_by_id(self, given_id):
        """
        Prints note by id
        """
        try:
            print([note for note in self.notes if str(note.note_id) == given_id][0])
        except IndexError:
            print("There are no notes with that id.")


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1" : self.show_notes,
            "2" : self.create_note,
            "3" : self.print_by_id,
            "4" : self.find_by_tag,
            "5" : self.find_by_text,
            "6" : self.modify_note,
            "7" : self.modify_tags,
            "8" : self.exit
        }

    def show_menu(self):
        print("The menu:\n"
              "1. Show all notes\n"
              "2. Create new note\n"
              "3. Print note by ID\n"
              "4. Find note by tags\n"
              "5. Find note by text\n"
              "6. Modify note by ID\n"
              "7. Modify tags by note ID\n"
              "8. Exit")
        return input("Your choice: ")

    def show_notes(self):
        print(self.notebook)
        self.notebook.print_notes()

    def create_note(self):
        while True:
            note = input("Text of new note: ")
            if note:
                break
        tags = input("Tags for new note (split them by space): ").split()
        self.notebook.new_note(note, tags)

    def print_by_id(self):
        id = input("Input the ID: ")
        self.notebook.print_note_by_id(id)

    def find_by_tag(self):
        tag = input("Input the tag: ")
        self.notebook.search_by_tags(tag)

    def find_by_text(self):
        text = input("Input the text: ")
        self.notebook.search_by_text(text)

    def modify_note(self):
        id = input("Input the ID: ")
        note = input("Input new note: ")
        self.notebook.modify_memo(id, note)

    def modify_tags(self):
        id = input("Input the ID: ")
        tags = input("Input new tags: ").split()
        self.notebook.modify_tags(id, tags)

    def run(self):
        while True:
            choice = self.show_menu()
            if choice in self.choices:
                self.choices[choice]()
            else:
                print(f"{choice} is not a valid choice")

    def exit(self):
        raise GeneratorExit
