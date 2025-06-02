# chapters/ch01.rpy
init:
    screen faq(adj): #Завтрашний я, знвй что ты долбаеб, который забил на оптимизацию и обещал ее сделать потот
        frame:
            xsize 1640
            xalign .5
            ysize 1085
            ypos 100

            has side "c r b"

            viewport:
                yadjustment adj
                mousewheel True
                draggable True

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
                            action Jump(label)
                            xfill True
                            
            bar adjustment adj style "vscrollbar"

            textbutton _("На этом пока все"):
                xfill True
                action Jump("specialnosty")
                top_margin 10

label chapter_01:
    
    scene bg window_1 # 1 (номер около bg - номер в раскадровке)
    gg "Экзамены уже прошли, пора бы уже задуматься куда поступать"
    pause

    scene bg notebook # 2
    show laptop_2
    # Ань тут хз как правильно оформить потом скажи как правильно написать

    gg "[dialogs['chapter_1']['home']['start']['text']]"
    $ add_note(
        notes['documents_for_admission'].title,
        notes['documents_for_admission'].text
    )

    # $ add_note("Требования для несовершеннолетних", "Если абитуриенту нет 18 лет, то обязательно надо ехать с родителем. У него с собой должен быть паспорт, Временная прописка (если есть)")
    gg "Тест базовый завершён (глянь заметки)"

    scene chema_beta
    menu way:
        "[dialogs['chapter_1']['home']['way_choice']['text']]"
        "Через Водный стадион":
            jump metro
        # "Моссельмаш": потом доделать, дедлайн горит
            # jump d3
        "Через Коптево":
            jump koptevo
        #"Лихоборы":  пока не трогаем, непопулярный маршрут, доделаем потом
        #    jump lihobory


label koptevo:
    scene bg koptevo_1  # 13 + 17
    pause

    menu choice_koptevo:
        "[dialogs['chapter_1']['koptevo']['way_choice']['text']]"
        "Через парк":  # Третий путь
            scene bg koptevo_tablo  # 14
            gg "О, я уже на станции «Коптево» и мне нужен первый выход" #29.05
            gg "Выхожу из МЦК и иду до перехода, в парк."
            scene bg koptevo_3  # 15
            gg "По навигатору мне нужно пройти прямо через парк мимо Головинских прудов, пока не дойду до колледжа."
            scene bg station_other_side  # 8
            pause
            scene bg kip_ost_ryadom
        "Чертов 72 автобус":  # Четвертый путь
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


label metro:
    scene bg vs_tablo  # выход из метро
    pause
    gg "О, уже «Водный стадион», мне нужен первый выход из метро." #29.05

    menu choice_vodniy:
        "Куда идем?"
        "Автобус":  # Первый путь
            gg "Мне нужно подняться вверх по эскалатору и прямо к остановке."
            scene bg vs_ost  # 7
            gg "[dialogs['chapter_1']['metro']['bus_dialog']['text']]"
            scene black with dissolve
            goida "[dialogs['chapter_1']['metro']['bus_dialog_2']['text']]"
            scene bg station_other_side with dissolve # 8
            pause
            scene bg kip_ost_ryadom
            gg "О, какой красивый колледж и так легко найти!"
        "Пешком":  # Второй путь
            gg "Мне нужно подняться вверх по эскалатору и повернуть налево."
            scene bg vs_pshkom  # 10
            gg "[dialogs['chapter_1']['metro']['walk_dialog']['text']]"
            scene bg kip_ost_ryadom
            gg "О, вот и колледж! Какой красивый и легко добраться!"

    jump security_dialog


label security_dialog:
    scene bg kipvhod # 26
    pause
    scene bg turnikety
    pause
    scene bg post_ohrany
    show ohrannik seriyezny
    gg "[dialogs['chapter_1']['security_dialog']['greeting']['text']]"
    security "[dialogs['chapter_1']['security_dialog']['security_response']['text']]"
    show ohrannik prov_docs
    gg "[dialogs['chapter_1']['security_dialog']['passport_request']['text']]"
    show ohrannik seriyezny
    security "[dialogs['chapter_1']['security_dialog']['directions']['text']]"
    hide security
    jump kabinet_103

    
label kabinet_103:
    scene bg 115_view # 29

    pause

    scene bg 103_view # 30

    pause

    scene bg dialog_103 with fade

    pause

    show kirill_smile

    gg "[dialogs['chapter_1']['kabinet_103']['greeting']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['form_question']['text']]"
    gg "[dialogs['chapter_1']['kabinet_103']['form_answer']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['form_instruction']['text']]"

    $ add_note(
        notes["data_for_application_form"].title,
        notes["data_for_application_form"].text
    )

    gg "[dialogs['chapter_1']['kabinet_103']['parent_data_question']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['parent_data_answer']['text']]"

    $ add_note(
        notes["parents_documents"].title,
        notes["parents_documents"].text
    )

    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['education_data_instruction']['text']]"

    $ add_note(
        notes["education_data_filling"].title,
        notes["education_data_filling"].text
    )
    jump FAQ

label FAQ:
    call screen faq(adj=ui.adjustment())
    jump specialnosty


label FAQ1:
    roditel "А вот вы, как студент данного колледжа, можете рассказать, каково здесь обучаться?"
    sotrudnic_103 "Хм… Обучение в Колледже Информатики и Программирования очень увлекательное, к тому же здесь я встретил много приятных и интересных людей."
    sotrudnic_103 "Мне все очень нравится, особенно возможность реализовывать свои проекты и применять знания на практике."
    jump start

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

label specialnosty:

    gg "Хорошо. Спасибо большое, что рассказали и ответили на наши вопросы"
    gg "А на какой специальности вы обучались?"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['specialties']['introduction']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['specialties']['information_systems']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['specialties']['information_security']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['specialties']['smart_systems']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['specialties']['telecom_security']['text']]"

    gg "Не уверен еще, могли бы вы рассказать подробнее о специальностях?"
    sotrudnic_103 "Вы можете выбрать несколько специальностей и поставить им разный приоритет."
    gg "Приоритет?"
    sotrudnic_103 "Вы будете участвовать в конкурсе аттестатов на несколько специальностей, но если проходите на все, то вас зачислит на специальность у которой приоритет выше."

    $ add_note(
        notes["transfer_to_budget"].title,
        notes["transfer_to_budget"].text
    )

    sotrudnic_103 "Вы будете поступать на бюджет или на платную основу?"
    menu choice_form:
            "Выбор бюджет/платка"
            "Бюджет":
                $ platka = False
            "Платное обучение":
                $ platka = True
    sotrudnic_103 "Хорошо, проходите в 115 кабинет!"
    gg "Спасибо, до свидания!"
    pause

    jump kabinet_115

label kabinet_115:
    scene bg 115_view with fade
    pause
    scene bg dialog_115 with fade
    pause
    show sotrudnic_115
    sotrudnic_115 "Добрый день! У вас есть какие-нибудь дипломы, сертификаты и прочее за последние 2 года?"
    sotrudnic_115 "Давайте ваши документы, которые вы указывали в 103 аудитории, я сделаю копии."
    sotrudnic_115 "Вы будете оставлять оригинал или копию аттестата? Если вы решите поступать в наш колледж на бюджет, то до конца работы приёмной комиссии нужно будет сдать оригинал, если на платную основу – оригинал надо оставить сразу."
    if platka:
        $ add_note(
            notes["tuition_payment"].title,
            notes["tuition_payment"].text
            )
    
    gg "Нам говорили про конкурс аттестатов, можете рассказать подробнее?"
    sotrudnic_115 "Конкурс аттестатов при поступлении в колледж — это рейтинг абитуриентов на основе среднего балла аттестата. Средний балл считается так: все оценки складывают и делят на количество предметов. Чем выше средний балл, тем лучше."
    sotrudnic_115 "Если мест меньше, чем желающих, берут тех, у кого больше баллов. Также если на последнее место претендует несколько человек с одним баллом будут учитываться грамоты."
    gg "А где можно найти этот список?"
    sotrudnic_115 "Списки можно посмотреть на сайте ({a=https://kip.fa.ru}https://kip.fa.ru{/a}), в разделе «Приёмная комиссия»."


    #menu choice_attectat:
        #    "А зачем тут выбор?"
        #    "Оставить копию аттестата":
        #        sotrudnic_115 "Заглушка"
        #    "Оставить оригинал":
        #        sotrudnic_115 "Заглушка"

    sotrudnic_115 "Следите за списками на сайте колледжа. Будем рады Вас видеть, удачи в поступлении!"
    
    gg "Спасибо, до свидания!"
    
    scene bg 115_view
    pause
    scene bg turnikety with fade
    pause
    scene bg kipvhod
    pause
    scene bg window_1 with fade
    pause
    scene bg notebook_goooool
    show laptop_2
    pause

    return
