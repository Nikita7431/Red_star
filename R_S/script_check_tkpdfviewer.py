import subprocess
import sys

def check_and_install_package(package_name):
    try:
        __import__(package_name)
        print(f"'{package_name}' уже установлен.")
    except ImportError:
        print(f"'{package_name}' не найден. Устанавливается...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"'{package_name}' успешно установлен.")

if __name__ == "__main__":
    check_and_install_package("tkPDFViewer")
