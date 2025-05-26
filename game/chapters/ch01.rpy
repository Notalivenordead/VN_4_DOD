# chapters/ch01.rpy

label chapter_01:
    
    scene bg window_1 # 1 (номер около bg - номер в раскадровке)

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
            goida "[dialogs['chapter_1']['koptevo']['park_dialog']['text']]"
            scene bg koptevo_3  # 15
            goida "[dialogs['chapter_1']['koptevo']['park_dialog']['text']]"
            scene bg station_other_side  # 8
            goida "[dialogs['chapter_1']['koptevo']['park_dialog']['text']]"
        "Чертов 72 автобус":  # Четвертый путь
            scene bg koptevo_alt_4  # 18
            goida "[dialogs['chapter_1']['koptevo']['bus72_dialog']['text']]"
            scene bg kopt_ost  # 19
            goida "[dialogs['chapter_1']['koptevo']['bus72_dialog']['text']]"

    jump empire_of_light


label lihobory: # Пятый путь
    scene bg lihobory_1 # в раскадровке 17 = bg koptevo

    goida "Идешь туда сюда и в кипе"

    scene bg lihobory_2 # в раскадровке 19 = bg koptevo_alt_5

    pause

    jump empire_of_light


label d3: # Шестой путь
    scene bg mosselmash_1 # 22

    goida "Идешь туда сюда и в кипе"

    scene bg mosselmash_2 # 23

    pause

    scene bg moss_ost # 24

    goida "Идешь туда сюда и в кипе"

    jump empire_of_light


label metro:
    scene bg vs_tablo  # выход из метро
    pause

    menu choice_vodniy:
        "Куда идем?"
        "Автобус":  # Первый путь
            scene bg vs_ost  # 7
            goida "[dialogs['chapter_1']['metro']['bus_dialog']['text']]"
            scene bg station_other_side  # 8
            goida "[dialogs['chapter_1']['metro']['bus_dialog_2']['text']]"
        "Пешком":  # Второй путь
            scene bg vs_pshkom  # 10
            goida "[dialogs['chapter_1']['metro']['walk_dialog']['text']]"

    jump empire_of_light


label empire_of_light:

    scene bg kip_ost_ryadom # 11

    pause

    scene bg kipvhod # 26

    pause


label security_dialog:
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

    roditel "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['food']['text']]"
    sotrudnic_103 "В столовой всегда можно найти разнообразные и вкусные блюда."

    gg "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['teachers']['text']]"
    sotrudnic_103 "Преподаватели отличные. Они знают свой предмет и умеют интересно его подавать."

    gg "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['schedule']['text']]"
    sotrudnic_103 "[dialogs['chapter_1']['kabinet_103']['additional_dialogs']['schedule_details']['text']]"

    gg "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['entrance_tests']['text']]"
    sotrudnic_103 "Нет, поступление происходит исключительно по вашему среднему баллу аттестата."

    roditel "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['school_certificate']['text']]"
    sotrudnic_103 "Справку можно получить после выхода приказа и зачисления."

    roditel "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['medical_certificate']['text']]"
    sotrudnic_103 "Все справки вы сдаёте после поступления вашему классному руководителю."

    roditel "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['military_deferral']['text']]"
    sotrudnic_103 "Да, будет."

    gg "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['campus_card']['text']]"
    sotrudnic_103 "Да."

    gg "[dialogs['chapter_1']['kabinet_103']['questions_about_college']['textbooks']['text']]"
    sotrudnic_103 "Учебники будут, но в небольшом количестве."

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
    
    #menu choice_form:
        #    "Выбор бюджет/платка"
        #    "Бюджет":
        #        sotrudnic_103 "Заглушка"
        #    "Платное обучение":
        #        sotrudnic_103 "Заглушка"

    sotrudnic_103 "Вы будете поступать на бюджет или на платную основу?"
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
