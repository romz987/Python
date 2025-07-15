from class_note import Note


class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)
        print("Записка добавлена")

    def remove_last_note(self):
        if self.notes:
            removed_note = self.notes.pop()
            print(f"Записка удалена")
        else:
            print("Нет записок для удаления.")

    def get_notes_list(self):
        if len(self.notes) > 0:
            return self.notes
