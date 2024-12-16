def write_and_read_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Успешно записано в файл '{filename}'.")
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()
        print(f"Успешно считано из файла '{filename}'.")
        return file_content
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except PermissionError:
        print(f"Ошибка: Нет доступа к файлу '{filename}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    filename = 'example.txt'
    content = 'Привет, мир! Это пример записи и чтения файла.'
    result = write_and_read_file(filename, content)
    if result is not None:
        print("\nСодержимое файла после записи и чтения:")
        print(result)
if __name__ == "__main__":
    main()
