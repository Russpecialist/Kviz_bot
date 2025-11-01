import os
import shutil

def clean_python_cache():
    for root, dirs, files in os.walk("."):
        # Удаляем папки __pycache__
        if "__pycache__" in dirs:
            cache_dir = os.path.join(root, "__pycache__")
            print(f"Удаляю: {cache_dir}")
            shutil.rmtree(cache_dir)
        
        # Удаляем .pyc файлы
        for file in files:
            if file.endswith(".pyc"):
                pyc_file = os.path.join(root, file)
                print(f"Удаляю: {pyc_file}")
                os.remove(pyc_file)

if __name__ == "__main__":
    clean_python_cache()
    print("Кэш очищен!")