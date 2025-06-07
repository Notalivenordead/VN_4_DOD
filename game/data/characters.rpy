# data/characters.rpy
init python:
    style.right_dialogue = Style(style.say_dialogue)
    style.right_dialogue.text_align = 1.0        # текст внутри блока по правому краю
    style.right_dialogue.xpos = 3150             # координата правого края блока (сдвиг влево)
    style.right_dialogue.xanchor = 1.0           # якорь справа (правый край блока — опорная точка)
    style.right_dialogue.box_wrap = True         # возможность смещения блока 
    style.right_dialogue.xmaximum = 2720         # ограничим ширину блока, чтобы не растягивался на весь экран

define kirill = Character('Кирилл', color="#b700ff")
define artem = Character('Артем', color="#9b6a00")
define idris = Character('Идрис', color="#007900")
define vera = Character('Вера', color="#b827fc")
define astra = Character('Астра', color="#e63600")
define nastya = Character('Настя', color="#17ffff")
define gg = Character('Абитуриент', color="#fdfdfd", who_xpos=1800, what_style="right_dialogue")
define gg_first = Character('Абитуриент (я)', color="#fdfdfd", who_xpos=1800)
define roditel = Character('Родитель', color="#fdfdfd", who_xpos=1800, what_style="right_dialogue")
define security = Character('Охранник', color="#ffc7c7")
define sotrudnic_103 = Character('Сотрудник из 103', color="#51fff0")
define sotrudnic_115 = Character('Сотрудник из 115', color="#ffcfcf")
define goida = Character('', color="#000000")
