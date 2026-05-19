# Think of a Text Editor's Undo Feature. Before you make a major change, the editor takes a "snapshot" of the current text and stores it in a small object (the Memento). If you realize you've made a mistake, the editor can reach back into its history and restore the previous state from that snapshot, effectively traveling back in time.

# Memento Pattern Implementation in Python
class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, new_text):
        self.text += new_text

    def save(self):
        return Memento(self.text)

    def restore(self, memento):
        self.text = memento.get_saved_text()
class Memento:
    def __init__(self, text):
        self._text = text

    def get_saved_text(self):
        return self._text
# Example usage:
editor = TextEditor()
editor.write("Hello, World!")
print(editor.text)  # Hello, World!
saved_state = editor.save()  # Save the current state
editor.write(" This is a Memento Pattern example.")
print(editor.text)  # Hello, World! This is a Memento Pattern example.
editor.restore(saved_state)  # Restore to the saved state
print(editor.text)  # Hello, World!, the text is restored to the previous state
editor.write(" Let's add more text.")
print(editor.text)  # Hello, World! Let's add more text., the text is updated again
editor.restore(saved_state)  # Restore again to the saved state
print(editor.text)  # Hello, World!, the text is restored again to the previous}}
    

    