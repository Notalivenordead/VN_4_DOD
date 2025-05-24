# script.rpy

# начальное состояние (sync store и тестовый персонаж)
default dialogs = {}
default notes = {}
default notes_user = {}
define test = Character('TEST', color="#eb9743")

# Инициализиацяи
init python:
    import json, os, renpy.store as store

    class Dialog:
        def __init__(self, text):
            self.text = text

    class Note:
        def __init__(self, title, text):
            self.title = title
            self.text = text
    
    dialogs = {}
    notes = {}

    # Путь к файлу JSON
    JSON_FILE_PATH = os.path.join(config.basedir, "game", "data", "data.json")

    # Функция для рекурсивного создания объектов Dialog
    def create_dialogs(data):
        if isinstance(data, dict):
            if "text" in data and isinstance(data["text"], str) and len(data) == 1:
                renpy.log(f"Преобразую в Dialog: {data['text'][:30]}...")
                return Dialog(data["text"])
            else:
                return {k: create_dialogs(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [create_dialogs(item) for item in data]
        return data


    # Загрузка данных из JSON
    def load_game_data():
        global dialogs, notes
        
        try:
            # Отладочное сообщение: проверяем путь
            renpy.log(f"Путь к файлу: {JSON_FILE_PATH}")
            
            # Проверяем существование файла
            if not os.path.exists(JSON_FILE_PATH):
                renpy.log(f"Файл не найден: {JSON_FILE_PATH}")
                return
            
            # Читаем JSON файл
            with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
                file_content = f.read()
                renpy.log(f"Содержимое файла (первые 200 символов): {file_content[:200]}...")  # Для отладки
                
                # Попытка парсинга JSON
                try:
                    data = json.loads(file_content)
                except Exception as e:
                    renpy.log(f"Ошибка при парсинге JSON: {str(e)}")
                    return
            
            # Отладочное сообщение
            renpy.log("JSON файл успешно загружен.")
            
            # Проверяем структуру JSON
            if "dialogs" not in data or "notes" not in data:
                renpy.log("Ошибка: В JSON отсутствуют ключи 'dialogs' или 'notes'.")
                return
            
            # Создание объектов Dialog из секции dialogs
            dialogs_raw = data.get("dialogs", {})
            renpy.log(f"Загружено исходных диалогов: {len(dialogs_raw)}")
            dialogs = create_dialogs(dialogs_raw)
            renpy.log(f"Загружено обработанных диалогов: {len(dialogs)}")
            
            # Создание объектов Note из секции notes
            notes_raw = data.get("notes", {})
            renpy.log(f"Загружено исходных записок: {len(notes_raw)}")
            notes = {}
            for note_id, note_data in notes_raw.items():
                notes[note_id] = Note(note_data["title"], note_data["text"])
            renpy.log(f"Загружено обработанных записок: {len(notes)}")
        
        except Exception as e:
            # Если произошла ошибка при загрузке
            renpy.log(f"Ошибка при загрузке данных: {str(e)}")


label start:
    python:
        import os, json
        load_game_data() # загрузка данных
        
        # Тест загрузки
        renpy.log(f"Путь {JSON_FILE_PATH}")
        renpy.log(f"Количество загруженных частей: {len(dialogs)}") 
        renpy.log(f"Количество загруженных локаций (часть 1): {len(dialogs['chapter_1'])}") 
        renpy.log(f"Количество загруженных записок: {len(notes)}\n")
        renpy.log("До примера (где текст)\n")
        renpy.log(dialogs['chapter_1']['kabinet_103']['greeting'])
        renpy.log("Прошёл пример")
        renpy.log("правильное использование\n")
        renpy.log(dialogs['chapter_1']['home']['start']['text'])
        renpy.log(test)


    call chapter_01
    call chapter_2
    return

