import string

cgreen = '\33[0;32m'
cend = '\033[0m'
cred = '\033[91m'

capital_letters = string.ascii_uppercase


def name_for_columns():
    columns_name = {}
    for i in capital_letters:
        name = input(f'Enter name for {cred}{i}{cend} column,\n'
                     f'if you want to stop - press {cred}ENTER twice{cend}' + '\n\n')
        if len(name) > 0:
            columns_name[i] = name
        else:
            break
    return columns_name


columns = name_for_columns()
print(columns)
