"""
data/notes.rpy
Заметки вместо подсказок (можно посмотреть всегда)
"""

init python:
    def add_note(title, text):
        # если уже есть заметка с таким заголовком — ничего не делать
        if title in store.notes_user:
            return
        store.notes_user[title] = Note(title, text)
        renpy.pause(0.2)
        renpy.show_screen("notification", title=title)

    def clear_notes():
        store.notes_user.clear()
