# Для запуска
# открыть терминал (PS)
# cd game
# python test.py
# посмотреть dump.txt (должен быть идентичен data.json за исключением "text"-метки)
# не должно быть ошибок при выполнении


import json 
import os # если нужно с путями работать
from pyparsing import Any # для нотации с Any

# Используемые классы (диалоги и записки)
class Dialog:
    def __init__(self, text):
        self.text = text


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text


# Путь к файлу JSON
JSON_FILE_PATH = "data/data.json" 

# 
def create_dialogs(data: Any) -> (Dialog | dict[Any, Dialog | dict | list[Dialog | dict | list | Any] | Any] | list[Dialog | dict | list | Any] | Any):
    if isinstance(data, dict):
        if "text" in data and isinstance(data["text"], str) and len(data) == 1:
            return Dialog(data["text"])
        else:
            return {k: create_dialogs(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [create_dialogs(item) for item in data]
    return data


# Загрузка данных из JSON
def  load_game_data() -> (tuple[dict, dict] | tuple[Dialog | dict[Any, Dialog | dict | Any] | Any, dict]):
    dialogs = {}
    notes = {}

    try:
        # Проверяем существование файла
        if not os.path.exists(JSON_FILE_PATH):
            print(f"Файл не найден: {JSON_FILE_PATH}")
            return dialogs, notes
        
        # Читаем JSON файл
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
            file_content = f.read()
            print(f"Содержимое файла (первые 200 символов): {file_content[:200]}...")  # Для отладки
            data = json.loads(file_content)  # Используем json.loads для парсинга строки

        print("JSON файл успешно загружен.")

        # Проверяем структуру JSON
        if "dialogs" not in data or "notes" not in data:
            print("Ошибка: В JSON отсутствуют ключи 'dialogs' или 'notes'.")
            return dialogs, notes

        # Создание объектов Dialog из секции dialogs
        dialogs_raw = data.get("dialogs", {})
        dialogs = create_dialogs(dialogs_raw)
        print(f"Загружено глав: {len(dialogs_raw)}")

        # Создание объектов Note из секции notes
        notes_raw = data.get("notes", {})
        notes = {}
        for note_id, note_data in notes_raw.items():
            notes[note_id] = Note(note_data["title"], note_data["text"])
        print(f"Загружено записок: {len(notes_raw)}")

    except Exception as e:
        # Если произошла ошибка при загрузке
        print(f"Ошибка при загрузке данных: {str(e)}")

    return dialogs, notes


def simple_serialize(obj):
            if isinstance(obj, dict):
                return {k: simple_serialize(v) for k, v in obj.items()}
            elif isinstance(obj, Dialog):
                return obj.text
            elif isinstance(obj, Note):
                return {
                    "title": obj.title,
                    "text": obj.text
                }
            elif hasattr(obj, "text"):
                return obj.text
            return str(obj)


# Проверяем содержимое словарей
def count_dialog_objects(obj):
    if isinstance(obj, Dialog):
        return 1
    elif isinstance(obj, dict):
        return sum(count_dialog_objects(v) for v in obj.values())
    elif isinstance(obj, list):
        return sum(count_dialog_objects(item) for item in obj)
    return 0


# Количество локаций локаций ВСЕГО
def count_locations(dialogs):
    count = 0
    for chapter in dialogs.values():
        if isinstance(chapter, dict):
            count += len(chapter)
    return count


# Тестовая функция
if __name__ == "__main__":
    # Загружаем данные
    dialogs, notes = load_game_data()

    # запись в файл полученной data
    with open("dump.txt", "w", encoding="utf-8") as f:
            json.dump({
                "dialogs": simple_serialize(dialogs),
                "notes": simple_serialize(notes)
            }, f, ensure_ascii=False, indent=2)

    # базовая информация
    print(f"Всего строк диалога: {count_dialog_objects(dialogs)}")
    print(f"Количество загруженных записок: {len(notes)}")
    print(f"Количество локаций: {count_locations(dialogs)}")

    # Пример использования диалога
    print("Пример использования диалога:")
    chapter_1 = dialogs.get("chapter_1", {})
    home = chapter_1.get("home", {})
    start_dialog = home.get("start", Dialog("Диалог не найден"))
    print(start_dialog.text)

    # Пример использования записки
    print("Пример использования записки:")
    documents_note = notes.get("documents_for_admission", Note("Заголовок не найден", "Текст не найден"))
    print(documents_note.title)
    print(documents_note.text)

    # доп...
    print(type(dialogs["chapter_1"]["kabinet_103"]["greeting"]))  # Должен быть <class 'Dialog'>
    print(dialogs["chapter_1"]["kabinet_103"]["greeting"].text)   # Должен быть текст "Здравствуйте."

