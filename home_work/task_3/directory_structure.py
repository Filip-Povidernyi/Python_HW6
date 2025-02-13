from colorama import Fore, Style
from pathlib import Path


def directory_structure(path: Path, divider: str = ""):
    try:
        # entries = sorted(path.iterdir(), key=lambda e: not e.is_dir(), e.name.lower())) (  # Сортування складових шляху (спочатку папки, потім файли)

        entries = list(path.iterdir())  # Без сортування

        for index, item in enumerate(entries):

            if index == len(entries) - 1:
                connector = "└── "
            else:
                connector = "├── "

            color = Fore.LIGHTMAGENTA_EX if item.is_dir() else Fore.CYAN
            name = f"📂 {item.name}" if item.is_dir() else f"📄 {item.name}"
            print(divider + connector + color + name + Style.RESET_ALL)

            if item.is_dir():

                extender = "    " if index == len(entries) - 1 else "│   "
                directory_structure(item, divider + extender)

    except PermissionError:

        print(Fore.RED + "[ACCESS DENIED]" + Style.RESET_ALL, path)
