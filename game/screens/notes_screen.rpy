# screens/notes_screen.rpy

screen notes_screen():
    tag menu
    modal True  # блокирование действия вне этого окна

    frame:
        style_prefix "pref"
        xalign 0.5
        yalign 0.5
        has vbox

        label "Заметки"

        if store.notes_user:
            for note in store.notes_user.values():
                textbutton note.title action [Show("note_detail", note=note), Hide("notes_screen")]
        else:
            text "Нет заметок."

        textbutton "Назад" action Hide("notes_screen")


screen note_detail(note):
    modal True

    frame:
        style_prefix "pref"
        xalign 0.5
        yalign 0.5
        has vbox

        label note.title
        text note.text

        textbutton "Назад" action [Show("notes_screen"), Hide("note_detail")]


screen notification(title):
    zorder 100
    timer 4.3 action Hide("notification") repeat False

    frame:
        xalign 0.5 
        yalign 0.1  
        background "#0008"
        has vbox

        text "Новая заметка: \"[title]\". Посмотреть можно в разделе \"Заметки\"."

