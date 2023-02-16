from pathlib import Path


def make_documets_folder(name):
    (Path.home() / "Documents" / f"{name}").mkdir(parents=True, exist_ok=True)

    return Path.home() / "Documents" / f"{name}"


if __name__ == '__main__':
    make_documets_folder(input("Enter the folder name\n\n"))
