from pathlib import Path

user_home_directory = Path.home()
list_of_files = Path.glob(user_home_directory,'*')
print(user_home_directory)
folders_voc = {}
count = 0
for i in list_of_files:
    if Path(i).is_dir() and Path(i).name.isalnum():
        folders_voc[count] = Path(i).name
        count += 1

for _ in folders_voc.items():
    print(_)