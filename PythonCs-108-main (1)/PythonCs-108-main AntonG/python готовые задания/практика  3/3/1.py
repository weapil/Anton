import os

def list_files_in_directory(directory_path):
    try:
        if not os.path.exists(directory_path):
            print(f"Ошибка: Каталог '{directory_path}' не существует.")
            return []
        if not os.path.isdir(directory_path):
            print(f"Ошибка: '{directory_path}' не является каталогом.")
            return []
        items = os.listdir(directory_path)
        files = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
        return files
    except PermissionError:
        print(f"Ошибка: Нет доступа к каталогу '{directory_path}'.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []
def main():
    directory = input("Введите путь к каталогу: ").strip()
    files = list_files_in_directory(directory)
    if files:
        print(f"\nФайлы в каталоге '{directory}':")
        for idx, file in enumerate(files, start=1):
            print(f"{idx}. {file}")
    else:
        print(f"В каталоге '{directory}' нет файлов или произошла ошибка.")
if __name__ == "__main__":
    main()
