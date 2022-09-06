from pathlib import Path
import os

# print(os.listdir(Path.home()))
print(Path.home())
# print(Path.home().iterdir())
folders = {}
count = 0
for i in Path.home().iterdir():
    if Path(i).is_dir() and Path(i).name.isalpha():
        count += 1
        folders[count] = Path(i).name
for i in folders.items():
    print(i)
# for _ in os.listdir(Path.home()):
#     print(_, Path(_).is_file())
        # print(_)

# way = (Path.home()/"Documents"/"PXP").mkdir(parents=True, exist_ok=True)