import os
from datetime import datetime

def file_stats(filepath):
    try:
        if not os.path.isfile(filepath):
            return {"error": f"Файл '{filepath}' не существует или это не файл."}
        size_bytes = os.path.getsize(filepath)
        modification_time = os.path.getmtime(filepath)
        readable_time = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
        base_name = os.path.basename(filepath)
        name, extension = os.path.splitext(base_name)
        extension = extension[1:] if extension.startswith('.') else extension
        return {
            'size_bytes': size_bytes,
            'last_modified': readable_time,
            'name': name,
            'extension': extension
        }
    except Exception as e:
        return {"error": f"Произошла ошибка при получении мета-данных файла: {e}"}

def main():
    filepath = input("Введите путь к файлу: ").strip()
    stats = file_stats(filepath)
    if 'error' in stats:
        print(f"Ошибка: {stats['error']}")
    else:
        print(f"\nМета-данные файла '{filepath}':")
        print(f"Размер: {stats['size_bytes']} байт")
        print(f"Последнее изменение: {stats['last_modified']}")
        print(f"Название: {stats['name']}")
        print(f"Расширение: {stats['extension']}")
if __name__ == "__main__":
    main()
