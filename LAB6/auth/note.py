"""
MODULE DOCSTRING
"""
from datetime import datetime


class Note:
    def __init__(self, memo, tags, note_id):
        self.memo = memo
        self.creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.tags = tags
        self.note_id = note_id

    def __str__(self):
        return f"'{self.memo}'\n" \
               f"Date created - {self.creation_date}\n" \
               f"Tags - {self.tags}\n" \
               f"Note id - {self.note_id}"

    def match(self, search_filter: str):
        """
        Checks match of the text
        """
        return search_filter in self.memo

    def tags_filter(self, search_filter: str):
        """
        Checks match with the tags
        """
        return search_filter in self.tags

    def id_match(self, given_id):
        """
        Checks, if the id matches with note
        """
        return given_id == self.note_id

    def memo_change(self, new_memo):
        """
        Changes teh memo
        """
        self.memo = new_memo

    def tags_change(self, new_tags):
        """
        Changes tags
        """
        self.tags = new_tags
