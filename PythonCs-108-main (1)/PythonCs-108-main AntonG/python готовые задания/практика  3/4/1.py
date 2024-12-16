from pathlib import Path

def ensure_directory_exists(directory_path):
    try:
        path = Path(directory_path)
        if path.exists():
            if path.is_dir():
                print(f"Каталог '{directory_path}' уже существует.")
                return True
            else:
                print(f"Ошибка: Путь '{directory_path}' существует, но не является каталогом.")
                return False
        else:
            path.mkdir(parents=True, exist_ok=False)
            print(f"Каталог '{directory_path}' успешно создан.")
            return True
    except PermissionError:
        print(f"Ошибка: Нет прав для создания каталога '{directory_path}'.")
        return False
    except Exception as e:
        print(f"Произошла ошибка при создании каталога '{directory_path}': {e}")
        return False

def main():
    directories = [
        'existing_directory',
        'new_folder/subfolder',
        '/root/protected_folder'
    ]
    for dir_path in directories:
        success = ensure_directory_exists(dir_path)
        if success:
            print(f"Операция для '{dir_path}' прошла успешно.\n")
        else:
            print(f"Операция для '{dir_path}' завершилась с ошибкой.\n")
if __name__ == "__main__":
    main()
