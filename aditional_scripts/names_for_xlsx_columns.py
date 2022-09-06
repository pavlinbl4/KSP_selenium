def name_for_columns():
    import string
    end = '\033[0m'
    red = '\033[91m'
    capital_letters = string.ascii_uppercase
    columns_name = {}
    for i in capital_letters:
        name = input(f'Enter name for {red}{i}{end} column,\n'
                     f'if you want to stop - press {red}ENTER twice{end}' + '\n\n')
        if len(name) > 0:
            columns_name[i] = name
        else:
            break
    print(columns_name)
    return columns_name


columns = name_for_columns()
