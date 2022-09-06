from pathlib import Path

print(Path.home())  #  print path to home directory

for i in Path.home().glob('*'):
    if Path(i).is_dir():
        print(i)
