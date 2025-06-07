# chapters/ch01.rpy
init python:
    renpy.music.register_channel("sound_2", "sfx", True)
init:
    screen maper():
        frame:
            padding (15, 25)
            xpos 500
            ypos 1800
            xsize 500
            textbutton _("Водный стадион"):
                xfill True
                action (Hide("maper"), Jump("metro"))
        frame:
            padding (15, 25)
            xpos 1630
            ypos 1770
            xsize 300
            textbutton _("Коптево"):
                xfill True
                action (Hide("maper"), Jump("koptevo"))

    screen docx():
        frame: 
            padding (10, 20)
            xalign 0.7
            yalign 0.6
            textbutton ("{size=+20}Отдать паспорт"):
                action Return()
            

    screen specialnosty_screen():
        
        frame:
            padding (15, 25)
            xsize 1240
            xalign .7
            yalign .25

            vbox:
                $ specialnost = [
                        ("Информационные системы и программирование ", "ISIP"),
                        ("Обеспечение информационной безопасности автоматизированных систем.", "OIBAS"),
                        ("Интеллектуальные интегрированные системы.", "IIS"),
                        ("Обеспечение информационной безопасности телекоммуникационных систем", "OIBTS")
                    ]

                for question, label in specialnost:
                    textbutton question:
                        action Jump(label)
                        xfill True
                textbutton _("На этом пока все"):
                    xfill True
                    action Jump("questions")
                    top_margin 10


    screen faq():
        
        modal True
        frame:
            padding (15, 25)
            xsize 1240
            xalign .8
            yalign .25
            vbox:
                $ faq_questions = [
                    ("А вот вы, как студент данного колледжа, можете рассказать, каково здесь обучаться?", "FAQ1"),
                    ("А в столовой вкусно кормят?", "FAQ2"),
                    ("Как обучают преподаватели? Понятно ли? Много ли к ним претензий?", "FAQ3"),
                    ("А во сколько начинаются и заканчиваются пары?", "FAQ4"),
                    ("Нужно ли писать вступительные?", "FAQ5"),
                    ("Как получить справку для школы о поступлении?", "FAQ7"),
                    ("Кому нужно будет сдать справку 086у?", "FAQ8"),
                    ("Будет ли отсрочка от армии?", "FAQ9"),
                    ("А кампусные карты у вас есть же? Я в группе в ВК видел. У меня такая будет?", "FAQ10"),
                    ("А тут также как и в школе будет куча учебников? Если да, то когда и где их забирать?", "FAQ11")
                ]
                for question, label in faq_questions:
                    textbutton question:
                        
                        action (Hide("faq"), Jump(label))
                        xfill True

                textbutton _("На этом пока все"):
                    xfill True
                    action (Hide("faq"), Jump("specialnosty"))
                    top_margin 10

label chapter_01:
    stop music fadeout 1.0

    queue music ["music_7.mp3", "music_8.mp3"] volume 0.5 fadein 1.0
    scene bg window_1 # 1 (номер около bg - номер в раскадровке)
    gg "Да, конечно. Всё верно."
    roditel "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc hendrerit nisl eu ex laoreet faucibus. Nulla volutpat mollis velit ut faucibus. Ut quis neque ut nunc rutrum ultricies sit amet."
    gg_first "Экзамены уже прошли, пора бы задуматься куда поступать"
    play sound_2 "tap_tap.mp3"
    scene bg procrpoiisk:
        yalign 0.0
    show laptop_2
    pause
    
    scene bg procrpoiisk: 
        yalign 0.0
        linear 1 yalign 1.07/6
    show laptop_2
    pause
    scene bg procrpoiisk:
        yalign 1.066/6
        linear 1 yalign 2.14/6
    show laptop_2
    pause
    scene bg procrpoiisk:
        yalign 2.14/6
        linear 1 yalign 3.21/6
    show laptop_2
    pause
    scene bg procrpoiisk:
        yalign 3.21/6
        linear 1 yalign 4.27/6
    show laptop_2
    pause
    scene bg procrpoiisk:
        yalign 4.27/6
        linear 1 yalign 5.34/6
    show laptop_2
    pause
    scene bg procrpoiisk:
        yalign 5.34/6
        linear 1 yalign 6.4/6
    show laptop_2
    pause
    stop sound_2 fadeout 1
    # Ань тут хз как правильно оформить потом скажи как правильно написать

    gg "Хм, КИПФИН выглядит хорошим и перспективным... Может попробовать подать документы в него?"
    $ add_note(
        notes['documents_for_admission'].title,
        notes['documents_for_admission'].text
    )

    $ add_note(
        "Несовершеннолетним",
        "Если абитуриенту нет 18 лет, то обязательно надо ехать с родителем. У него с собой должен быть паспорт, Временная прописка (если есть)"
    )
    scene bg map
    call screen maper()




label koptevo:
    scene black  # 13 + 17
    pause

    menu choice_koptevo:
        "[dialogs['chapter_1']['koptevo']['way_choice']['text']]"
        "Через парк":  # Третий путь
            scene bg koptevo_tablo  # 14
            gg "О, я уже на станции «Коптево» и мне нужен первый выход" #29.05
            gg "Выхожу из МЦК и иду до перехода, в парк."
            scene bg koptevo_3  # 15
            gg "По навигатору мне нужно пройти прямо через парк мимо Головинских прудов, пока не дойду до колледжа."
            scene bg kip_ost_napr  # 8
            pause
            scene bg kip_ost_ryadom
        "Автобус 72":  # Четвертый путь
            gg "О, я уже на станции «Коптево» и мне нужен второй выход."
            scene bg koptevo_alt_4  # 18
            gg "По навигатору мне нужно выйти из МЦК и повернуть налево, пройдя на остановку «Проезд Черепановых»"
            scene bg kopt_ost  # 
            pause
            scene black with dissolve
            goida "Объявление остановки: Улица Лавочкина, храм Иоанна Кронштадтского."
            scene bg kip_ost_ryadom with dissolve
    gg "О, вот и колледж! Какой красивый и легко добраться!"
    
    jump security_dialog

"""
label lihobory: # Пятый путь
    scene bg lihobory_1 # в раскадровке 17 = bg koptevo

    goida "Идешь туда сюда и в кипе"

    scene bg lihobory_2 # в раскадровке 19 = bg koptevo_alt_5

    pause

    jump security_dialog


label d3: # Шестой путь
    scene bg mosselmash_1 # 22

    goida "Идешь туда сюда и в кипе"

    scene bg mosselmash_2 # 23

    pause

    scene bg moss_ost # 24

    goida "Идешь туда сюда и в кипе"

    jump security_dialog
"""

label metro:
    scene bg vs_tablo  # выход из метро
    stop music fadeout 1
    play sound "metro.mp3" volume 0.3
    pause
    gg "О, уже «Водный стадион», мне нужен первый выход из метро." #29.05

    menu choice_vodniy:
        "Куда идем?"
        "Автобус":  # Первый путь
            gg "Мне нужно подняться вверх по эскалатору и прямо к остановке."
            stop sound fadeout 1
            queue music ["music_8.mp3", "music_7.mp3"] volume 0.5 fadein 1
            scene bg vs_ost  # 7
            gg "[dialogs['chapter_1']['metro']['bus_dialog']['text']]"
            scene black with dissolve
            goida "[dialogs['chapter_1']['metro']['bus_dialog_2']['text']]"
            scene bg kip_ost_napr with dissolve # 8
            pause
            scene bg kip_ost_ryadom
            
            gg "О, какой красивый колледж и так легко найти!"
        "Пешком":  # Второй путь
            gg "Мне нужно подняться вверх по эскалатору и повернуть налево."
            play sound "street_sound.mp3" volume 0.4 fadein 1 fadeout 1
            scene bg vs_pshkom  # 10
            gg "[dialogs['chapter_1']['metro']['walk_dialog']['text']]"
            stop sound fadeout 1
            queue music ["music_8.mp3", "music_7.mp3"] volume 0.5
            scene bg kip_ost_ryadom
            gg "О, вот и колледж! Какой красивый и легко добраться!"

    jump security_dialog


label security_dialog:
    scene bg kipvhod with fade
    pause
    scene bg turnikety with fade
    pause
    scene bg post_ohrany
    show ohrannik seriyezny with dissolve
    security "Здравствуйте."
    gg "Здравствуйте, куда нужно пройти, чтобы попасть в приёмную комиссию?"
    security "Чтобы подать документы нужно пройти в 103 кабинет. Можно ваш паспорт, пожалуйста."
    call screen docx()
    gg "Да, конечно."
    show ohrannik prov_docs
    pause
    show ohrannik seriyezny
    security "Всё хорошо, вам от турникетов налево до конца коридора."
    hide security
    jump kabinet_103

    
label kabinet_103:
    scene bg 115_view # 29
    gg "Сначала мне нужно пройти налево в 103 кабинет, а в 115 я еще вернусь "

    scene bg 103_view # 30

    pause
    play sound "door_open.mp3"
    scene bg 103 with fade
    play music "music_10.mp3" fadeout 0.5 fadein 1 volume 0.4

    pause

    image kirill:
        "kirill_smile" with dissolve
        pause 20.0
        "kirill_vbok" with dissolve
        pause 5.0
        repeat
    show kirill

    gg "[dialogs['chapter_1']['kabinet_103']['greeting']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['form_question']['text']]"
    gg "[dialogs['chapter_1']['kabinet_103']['form_answer']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['form_instruction']['text']]"
    play sound_2 "tap_tap.mp3"

    scene spritepit:
        yalign -0.004
    show bg pk_kip
    pause
    
    scene spritepit:
        yalign 0.0
        linear 1 yalign 1.08/10
    show bg pk_kip
    pause


    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['form_warning']['text']]"
    $ add_note(
        notes["data_for_application_form"].title,
        notes["data_for_application_form"].text
    )
    scene spritepit:
        yalign 1.08/10
        linear 1 yalign 2.20/10
    show bg pk_kip
    pause
    
    gg "[dialogs['chapter_1']['kabinet_103']['parent_data_question']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['parent_data_answer']['text']]"

    $ add_note(
        notes["parents_documents"].title,
        notes["parents_documents"].text
    )
    scene spritepit:
        yalign 2.20/10
        linear 1 yalign 3.303/10
    show bg pk_kip
    pause
    scene spritepit:
        yalign 3.303/10
        linear 1 yalign 4.408/10
    show bg pk_kip
    pause
    scene spritepit:
        yalign 4.408/10
        linear 1 yalign 5.510/10
    show bg pk_kip
    pause
    scene spritepit:
        yalign 5.510/10
        linear 1 yalign 6.613/10
    show bg pk_kip
    pause
    scene spritepit:
        yalign 6.613/10
        linear 1 yalign 7.717/10
    show bg pk_kip
    pause
    stop sound_2 fadeout 1
    $ add_note(
        notes["education_data_filling"].title,
        notes["education_data_filling"].text
    )
    
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['education_data_instruction']['text']]"
    scene spritepit:
        yalign 7.717/10
        linear 1 yalign 8.82/10
    show bg pk_kip
    pause
    

    
    jump FAQ

label FAQ:
    show kirill
    
    show screen faq()
    sotrudnic_103 "У вас остались какие-нибудь вопросы?"
    jump FAQ


label FAQ1:
    roditel "А вот вы, как студент данного колледжа, можете рассказать, каково здесь обучаться?"
    sotrudnic_103 "Хм… Обучение в Колледже Информатики и Программирования очень увлекательное, к тому же здесь я встретил много приятных и интересных людей."
    sotrudnic_103 "Мне все очень нравится, особенно возможность реализовывать свои проекты и применять знания на практике."
    jump FAQ

label FAQ2:
    gg "А в столовой вкусно кормят?"
    sotrudnic_103 "В  столовой всегда можно найти разнообразные и вкусные блюда, у нас есть комплексный обед, также меню меняется в зависимости от дня недели. Я и мои друзья всегда находим что-то по душе."
    sotrudnic_103 "Еще перекусить можно в кофейне около столовой или в ближайших магазинах."
    jump FAQ
label FAQ3:
    roditel "Как обучают преподаватели? Понятно ли? Много ли к ним претензий?"
    sotrudnic_103 "Преподаватели отличные. Они знают свой предмет и при этом умеют интересно его подавать. Жалобы, если и бывают, то редкие, не бывает же идеальных людей, верно?"
    jump FAQ
label FAQ4:
    gg "А во сколько начинаются и заканчиваются пары?"
    sotrudnic_103 "Первая пара начинается в 8:30, восьмая пара заканчивается в 20:40. Хочу заметить, что не обязательно вы будете начинать и заканчивать в это время."
    sotrudnic_103 "У первых курсов максимум 5 пар до 17:20, старшие же курсы могут начать обучаться в 14:00 и закончить к семи. Это будет зависеть от расписания, которое составят вашей группе."
    jump FAQ
label FAQ5:
    gg "Нужно ли писать вступительные?"
    sotrudnic_103 "Нет, поступление происходит исключительно по вашему среднему баллу аттестата."
    jump FAQ
label FAQ7:
    roditel "Как получить справку для школы о поступлении?"
    sotrudnic_103 "Справку можно получить после выхода приказа и зачисления. На нашем сайте (https://kip.fa.ru) можно её заказать."
    jump FAQ
label FAQ8:
    roditel "Кому нужно будет сдать справку 086у? "
    sotrudnic_103 "Все справки вы сдаёте после поступления вашему классному руководителю."
    jump FAQ
label FAQ9:
    roditel "Будет ли отсрочка от армии? "
    sotrudnic_103 "Да, будет."
    jump FAQ
label FAQ10:
    gg "А кампусные карты у вас есть же? Я в группе в ВК видел. У меня такая будет? "
    sotrudnic_103 "Да."
    jump FAQ
label FAQ11:
    gg "А тут также как и в школе будет куча учебников? Если да, то когда и где их забирать?"
    sotrudnic_103 "Учебники будут, но в небольшом количестве. Обычно их выдают на занятиях или предоставляют в электронном формате. Хотя, если надо, их можно взять в нашей библиотеке."
    jump FAQ

label ISIP:
    sotrudnic_103 "На этой специальности изучают такие языки, как C++, C# и Java и многие другие, чтобы создавать программы для Windows и Linux, а также писать различные сайты. В основном мы работаем в Visual Studio и часто создаем свои собственные программы. "
    sotrudnic_103 "Срок обучения составляет 3 года и 10 месяцев. После окончания колледжа вы получаете профессию  – программист."
    jump special
label OIBAS:
    sotrudnic_103 "На этом направлении вы будете изучать законодательную базу защиты информации, научитесь защищать информацию в компаниях и разбираться в шифрах, а также  узнаете, как устанавливать камеры, датчики и сигнализации, сможете ставить программы, и настраивать их так, чтобы доступ к информации был только у вас. После учёбы получите профессию техника по безопасности. Срок обучения составляет 3 года и 10 месяцев."
    jump special
label IIS:
    sotrudnic_103 "На этой специальности вы научитесь управлять разными устройствами с помощью компьютера, наподобие Умного дома. Вы узнаете, как объединять части программ, исправлять ошибки и делать так, чтобы программы и техника работали вместе. После окончания колледжа вы станете техником по умным системам. На эту специальность нужно учиться 2 года и 10 месяцев."
    jump special
label OIBTS:
    sotrudnic_103 "На данный момент можно поступить только на бюджет. После колледжа вы сможете работать техником по защите информации. Вы будете управлять рисками информационной безопасности, определять уязвимости и угрозы моделированием системы защиты информации, а также организацией защиты сетей связи. Срок обучения составляет 3 года и 10 месяцев."
    jump special

label specialnosty:

    gg "Нет, мы узнали все, что хотели. Спасибо большое, что рассказали и ответили на наши вопросы!"
    gg "А на какой специальности вы обучались?"
    sotrudnic_103 "Я учусь на специальности Информационные системы и программирование."
    sotrudnic_103 "На какую специальность вы собираетесь поступать?"
    gg "Не уверен еще, могли бы вы рассказать подробнее о специальностях?"
    jump special

label special:
    call screen specialnosty_screen()

label questions:
    sotrudnic_103 "Вы можете выбрать несколько специальностей и поставить им разный приоритет."
    gg "Приоритет?"
    sotrudnic_103 "Вы будете участвовать в конкурсе аттестатов на несколько специальностей, но если проходите на все, то вас зачислит на специальность у которой приоритет выше."

    $ add_note(
        notes["transfer_to_budget"].title,
        notes["transfer_to_budget"].text
    )

    
    menu choice_form:
            sotrudnic_103 "Вы будете поступать на бюджет или на платную основу?"
            "Бюджет":
                $ platka = False
            "Платное обучение":
                #$ add_note(
                #    "Заметка 563",
                #    "На специальностях ИСИП, ОИБАС, ИИС в будущем можно перевестись на бюджет только после 2 курса."
                #)
                $ platka = True
    sotrudnic_103 "Хорошо, мы всё заполнили, можете проходить в 115 кабинет!"
    gg "Спасибо, до свидания!"

    jump kabinet_115

label kabinet_115:
    scene bg 115_view with fade
    pause
    play sound "door_knock.mp3"
    scene bg 115 with fade
    play music "music_10.mp3" fadeout 0.5 fadein 1 volume 0.4
    pause
    image sotr_115:
        "sotrudnic_115_smile" with dissolve
        pause 15.0
        "sotrudnic_115" with dissolve
        pause 3.0
        repeat
    show sotr_115 
    sotrudnic_115 " Добрый день! Вы уже заполнили анкету в 103 кабинете? "
    gg "Да, все заполнено."
    
    menu choice_sertificate:
        sotrudnic_115 "Отлично. У вас есть какие-нибудь дипломы, сертификаты и прочее за последние 2 года?"
        "Да":
            sotrudnic_115 "Отлично. Пожалуйста, давайте их и ваши документы, которые вы указывали в 103 аудитории, я сделаю копии."
        "Нет":
            sotrudnic_115 "Ничего страшного. Пожалуйста, давайте ваши документы, которые вы указывали в 103 аудитории, я сделаю копии."
    
    if platka:
        $ add_note(
            notes["tuition_payment"].title,
            notes["tuition_payment"].text
            )
        sotrudnic_115 "Вы можете сами выбрать как будете оплачивать обучение, но при заключении договора вы сразу оплачиваете минимально первый семестр обучения. Это можно сделать: С помощью квитанции через оператора банка, через терминал, с помощью системы онлайн-оплаты, с квитанцией в самом банке."
        sotrudnic_115 "Оплатить обучение возможно материнским капиталом. В данном случае заключается дополнительное соглашение на оплату по мат. Капиталу. Для этого надо иметь при себе оригинал сертификата. После заключения выдаются бумаги для пенсионного фонда. Важно! Им можно оплатить как всю сумму, так и часть. Данные средства идут долго, месяц-два."
        sotrudnic_115 "После заключения договора, чек об оплате обучения за 1 семестр необходимо выслать на электронную почту приемной комиссии: KIPFINpriemka@fa.ru"
        sotrudnic_115 "Также договор можно расторгнуть и средства, которыми вы оплатили обучение, вернутся."
    else:
        gg "Нам говорили про конкурс аттестатов, можете рассказать подробнее?"
        sotrudnic_115 "Конкурс аттестатов при поступлении в колледж — это рейтинг абитуриентов на основе среднего балла аттестата. Средний балл считается так: все оценки складывают и делят на количество предметов. Чем больше средний балл, тем лучше."
        sotrudnic_115 "Если мест меньше, чем желающих, берут тех, у кого больше баллов. Также если на последнее место претендует несколько человек с одним баллом будут учитываться грамоты."
        gg "А где можно найти этот список?"
        sotrudnic_115 "Списки можно посмотреть на сайте ({a=https://kip.fa.ru}https://kip.fa.ru{/a}), в разделе «Приёмная комиссия»."

        menu choice_attectat:
            sotrudnic_115 "Вы будете оставлять оригинал или копию аттестата? Если вы решите поступать в наш колледж на бюджет, то до конца работы приёмной комиссии нужно будет привезти и сдать оригинал, если на платную основу – оригинал надо оставить сразу."
            "Оставить копию аттестата":
                sotrudnic_115 "Не забудьте до конца приемной комиссии оставить оригинал. Будем рады Вас видеть, удачи в поступлении!"
            "Оставить оригинал":
                sotrudnic_115 "Следите за списками на сайте колледжа. Будем рады Вас видеть, удачи в поступлении!"

    
    
    gg "Спасибо, до свидания!"
    
    scene bg 115_view with fade
    pause
    scene bg turnikety with fade
    pause
    scene bg kipvhod with fade
    pause
    scene bg window_1 with fade
    gg "Надо посмотреть приказы о зачислении на сайте колледжа."
    scene bg laptopfinal
    gg "О, отлично! Я поступил!"

    return
