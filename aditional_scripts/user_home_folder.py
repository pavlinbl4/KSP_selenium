from pathlib import Path


class HomeFolder:
    def __init__(self):
        self.user_home_directory = Path.home()
        self.list_of_files = Path.glob(Path.home(), '*')
        self.folders_voc = {}
        count = 0
        for i in self.list_of_files:
            if Path(i).is_dir() and Path(i).name.isalnum():
                self.folders_voc[count] = Path(i).name
                count += 1

    def make_path(self, subfolder_name, folder_number):
        self.subfolder_name = subfolder_name
        self.folder_number = folder_number
        return f'{home.user_home_directory}/{home.folders_voc[2]}/{home.subfolder_name}'

    def add_subfolder_to_kommersant(self, subfolder_name):
        self.subfolder_name = subfolder_name
        return f'{home.user_home_directory}/Documents/Kommersant/{home.subfolder_name}'


home = HomeFolder()
home.make_path('test',0)
