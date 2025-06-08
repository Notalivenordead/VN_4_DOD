# data/characters.rpy
init python:
    style.right_dialogue = Style(style.say_dialogue)
    style.right_dialogue.text_align = 1.0        # текст внутри блока по правому краю
    style.right_dialogue.xpos = 3150             # координата правого края блока (сдвиг влево)
    style.right_dialogue.xanchor = 1.0           # якорь справа (правый край блока — опорная точка)
    style.right_dialogue.box_wrap = True         # возможность смещения блока 
    style.right_dialogue.xmaximum = 2720         # ограничим ширину блока, чтобы не растягивался на весь экран

    style.right_name = Style(style.say_label)
    style.right_name.text_align = 1.0        # текст внутри блока по правому краю
    style.right_name.xpos = 2400             # координата правого края блока (сдвиг влево)
    style.right_name.xanchor = 1.0           # якорь справа (правый край блока — опорная точка)

   
define kirill = Character('Кирилл', color="#93cbd5")
define artem = Character('Артем', color="#9b6a00")
define idris = Character('Идрис', color="#007900")
define vera = Character('Вера', color="#b827fc")
define astra = Character('Астра', color="#e63600")
define nastya = Character('Настя', color="#17ffff")
define gg = Character('Абитуриент', color="#fdfdfd", who_style="right_name", what_style="right_dialogue")
define gg_first = Character('Абитуриент (я)', color="#fdfdfd", who_style="right_name", what_style="right_dialogue")
define roditel = Character('Родитель', color="#fdfdfd", who_style="right_name", what_style="right_dialogue")
define security = Character('Охранник', color="#82a4cf")
define sotrudnic_103 = Character('Сотрудник из 103', color="#93cbd5")
define sotrudnic_115 = Character('Сотрудник из 115', color="#bb8da7")
define goida = Character('', color="#000000")
