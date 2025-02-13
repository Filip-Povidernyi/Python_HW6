from pathlib import Path
import sys
from colorama import init, Fore, Style
from directory_structure import directory_structure as directory_viewer


def main():

    init(autoreset=True)

    if len(sys.argv) != 2:

        print(
            Fore.RED + "Введіть: python home_work/task_3/path_tree.py [Ваш шлях до директорії]" + Style.RESET_ALL)
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists() or not path.is_dir():

        print(
            Fore.RED + "Такого шляху до директорії не існує! Перевірте." + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.GREEN + f"📦 {path} " + Style.RESET_ALL)
    directory_viewer(path)


if __name__ == "__main__":
    main()
