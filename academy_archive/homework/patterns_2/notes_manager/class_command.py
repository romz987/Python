from class_note import Note
from class_note_manager import NoteManager


class AddNoteCommand:


    def __init__(self, note_manager: NoteManager, note: Note):
        self.note_manager = note_manager
        self.note = note


    def execute(self):
        self.note_manager.add_note(self.note)


    def undo(self):
        self.note_manager.remove_last_note()
