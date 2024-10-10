from colorama import Fore
import os
import re
import time
import threading
from datetime import date

ascii = '''

▒▒▒▒ ███ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░   ▒▒▒▒ ▓▓██    ▒▒▒▒▒▒▒▒▒▒▒▒ ▓██████ ▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒█▒▒▒▒ ▒▒▒▒ █
▒░██████▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒   ▒▒▒▒ ▓▓███    ▒▒▒▒▒▒▒▒▒▒▒▒ ▓███████ ▒▒▒▒    ░▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒ ▒▒  ▒▒▒▒░█
███████▒▒▒▒▒▒▒░ ▒▒▒▒▒▒▒▒    ▒▒▒▒▓▓████▓    ▒▒▒▒▒▒▒▒▒▒▒░█████████░▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒  ▒▒▒▒▒█
██████ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒    ▒▒▒ ▓▓█████     ▒▒▒▒▒▒▒▒▒▒▒██████████▒▒▒▒█    ▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒   ▒▒▒▒▒█
██████▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒░    ▒▒▒▓▓██████     ▒▒▒▒▒▒▒▒▒▒▒███████████▒▒▒██   ▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒   ▒▒▒▒▒█
█████ ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒     ▒▒░▓▓██████░    █▒▒▒▒▒▒▒▒▒▒████████████▒▒ ██   ▒▒▒▒▒▒▒▒▒▒▒▒  ░▒▒  ▒▒▒▒░█
█████▒▒▒ ▒▒▒   ▒▒▒▒▒▒▒░     ▒▒▓▓████████    █ ▒▒▒▒▒▒▒▒▒█████████████▒ ███  ▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒  ▒▒▒▒ █
████ ▒▒  ▒▒▒   ▒▒▒▒▒▒▒     ▓▒ ▓▓████████    ██ ▒▒▒▒▒▒▒▒█████████████▓░████  ▒▒▒▒▒▒▒▒▒▒▒    ▒▒ ▒▒▒▒ █
████▒▒▒█░▒▒    ▒▒▒▒▒▒▒    ▓█░▓░        ██   ███░▒▒▒▒▒▒▒██           ▒░█████ ▒▒▒▒▒▒▒▒▒▒▒     ▒ ▒▒▒▒██
███ ▒▒██▒▒▒    ▒▒▒▒▒▒░   ▒▓   ▒        ██   ████▒▒▒▒▒▒▒██████             ░  ▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒░██
███ ▒ ██▒▒░    ░▒▒▒▒▒    ▓█ ██         ███  █████▒▒▒▒▒▒ ████                 ▒▒▒▒▒▒▒▒▒▒      ▒ ▒▒ ██
███▒▒███▒▒      ▒▒▒▒▒    ▓██ █         ▓██  █████▓▒▒▒▒▒ ████                  ▒▒▒▒▒▒▒▒▒       ▒▒▒███
███▒ ███▒▒      ▒▒▒▒▒    ▒██ █       █  ███ ██████▒▒▒▒▒ ████        ▒         ░▒▒▒▒▒▒▒▒      ░   ███
███▒████░▒      ░▒▒▒▒     █████  ▓   ▓  ███ ███████▓▒▒▒▒████   ▓    ▓  █       ▒▒▒▒▒▒▒▒      ░▒▒████
██░ ████ ▒      ▒▒▒▒░     ▓██░████   ▓  █████████████▒▒▒████████▓  ▓▓          ░▒▒▒▒▒▒▒█     ▒▒  ███
██ ▒████ ▒     ██░▒▒░      ████  ▓▓▓ ▓████████████████░▒░███▒ ▓▓▓▓▓▓▒ █         ▒▒▒▒▒▒░██    ▒▒  ███
██ ██████▒     ███▒▒░      █████   ▓▓  ░███████████████░ ████  ▓▓▒▓▓███          ▒▒▒▒▒ ██    ▒▒▒████
█████████░    ████ ▒░       █████   █████████████████████████▒       █           ▒▒▒▒▒▒██    ▒▒█████
█████████ ░   █████▒░▒      ██████████████████████████████████████████           ░▒▒▒▒██     ▒▒█████
██████████░  ███████▒█      ████████████████████████████████████████              ▒▒▒ █      ▒▒█████
'''

# Создание файла с логами
current_date = date.today().strftime("%Y-%m-%d")
current_dir = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(current_dir, f'логи_{current_date}.txt')
with open(full_path, 'a+', encoding='utf-8') as logs:
    logs.write(f'\n└⊰ ✫  ⊱──⊰ ✫  ⊱──⊰ ✫  ⊱┘')
    logs.write(f'\nЛоги с {current_date}')


# Разделение текста
sep= Fore.MAGENTA + '└⊰ ✫  ⊱─────────────────────────────────⊰ ✫  ⊱─────────────────────────────────⊰ ✫  ⊱┘' + Fore.RESET

# Функция для очистки экрана
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

# Вывод ASCII-арта
print(Fore.MAGENTA + ascii + Fore.RESET)
print(sep)
print()

# Ввод директории базы данных
print(Fore.GREEN + 'Введите путь без кавычек и иных символов' +  Fore.RESET)
db_directory = input(f"{Fore.CYAN}(*) Введите полный путь директории: {Fore.RESET}")

# Проверка наличия .txt файлов в директории
files = [f for f in os.listdir(db_directory) if f.endswith('.txt')]

# Вывод списка доступных баз данных
print(Fore.MAGENTA + "(*)" + " Доступные базы данных:" + Fore.RESET)

for i, file in enumerate(files, 1):
    print(f"{i}. {file}")

# Выбор базы данных
while True:
    user_input = input(Fore.CYAN + "(*)" + " Выберите базу данных: " + Fore.RESET)
    try:
        choice = int(user_input) - 1
        if 0 <= choice < len(files):
            selected_filename = files[choice]
            with open(full_path, 'a+', encoding='utf-8') as logs:
                logs.write(f'\n(*) Выбранная база данных: {selected_filename}')
            break
        # Если введены некорректные данные
        else:
            print(f"{Fore.RED}Номер не был найден в списке. Σ(°ロ°){Fore.RESET}")
    except ValueError:
        print(f"{Fore.RED}Было введёно некорректное значение. Σ(°ロ°){Fore.RESET}")

# Выбор файла из списка
selected_file = os.path.join(db_directory, files[choice])

# Таймер
global elapsed_seconds
elapsed_seconds = 0

def timer():
    global stop_timer, elapsed_seconds
    while not stop_timer:
        time.sleep(1)
        elapsed_seconds += 1

# Ввод значения для поиска
search_value = input(f"{Fore.CYAN}(*) Введите значение для поиска: {Fore.RESET}")
with open(full_path, 'a+', encoding='utf-8') as logs:
                    logs.write(f'\n(*) Введено значение для поиска: {search_value}')

# Таймер
stop_timer = False
timer_thread = threading.Thread(target=timer)
timer_thread.start()

# Поиск значения в файле
try:
    with open(selected_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            if search_value in line:
                print(f"\n{Fore.GREEN}(+) Найдено в строке {line_number}:{Fore.RESET}")
                print(f"{line.strip()}")
                logs = open(f'логи_{current_date}.txt', 'a+')
                with open(full_path, 'a+', encoding='utf-8') as logs:
                    logs.write(f'\n{line}')
except KeyboardInterrupt:
    print(f"\n{Fore.YELLOW}(*) Поиск прерван пользователем.{Fore.RESET}")
    with open(full_path, 'a+', encoding='utf-8') as logs:
                    logs.write(f'\n(*) Поиск прерван пользователем.')

# Завершение таймера
finally:
    stop_timer = True
    timer_thread.join()

# Сохранение логов и вывод сообщения о завершении поиска
print()
print(sep)
print(f"\n{Fore.MAGENTA}(*) Логи были сохранены в пути: {Fore.RESET}{full_path}")
print(f"{Fore.GREEN}(*) Поиск завершен. Прошло: {Fore.RESET}{elapsed_seconds - 1} сек.")
with open(full_path, 'a+', encoding='utf-8') as logs:
                    logs.write(f'(*) Поиск завершен.')

# Закрытие файла логов
logs.close()